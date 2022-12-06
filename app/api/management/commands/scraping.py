from django.conf import settings
from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from api.models import *
from bs4 import BeautifulSoup
import requests

def machine_learning():
    print("Machine Learning")

def stock_scraping():
    security_codes = settings.SECURITY_CODE
    for code in security_codes:
      response = requests.get('https://kabutan.jp/stock/kabuka?code=' + code)
      soup = BeautifulSoup(response.text, 'html.parser')
      today = soup.find('table', {'class': 'stock_kabuka0'}).find('tbody').find_all('td')
      yesterday = soup.find('table', {'class': 'stock_kabuka_dwm'}).find('tbody').find('tr').find_all('td')

      # 今日の株価データが無ければ追加
      Price.objects.get_or_create(
          date=date.today(),
          defaults={
              "open": float(today[0].text.replace(",", "")),
              "high": float(today[1].text.replace(",", "")),
              "low": float(today[2].text.replace(",", "")),
              "close": float(today[3].text.replace(",", "")),
              "stock_id": code
          }
      )
      # 昨日の株価データがあれば更新、無ければ追加
      Price.objects.update_or_create(
          date=date.today() - relativedelta(days=1),
          defaults={
              "open": float(yesterday[0].text.replace(",", "")),
              "high": float(yesterday[1].text.replace(",", "")),
              "low": float(yesterday[2].text.replace(",", "")),
              "close": float(yesterday[3].text.replace(",", "")),
              "stock_id": code
          }
      )

class Command(BaseCommand):
    def handle(self, *args, **options):
        stock_scraping()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(stock_scraping, 'cron', hour=9, day_of_week='mon-fri', misfire_grace_time=300)# 毎日9時00分に実行
    scheduler.start()
