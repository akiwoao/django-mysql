from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, date
from bs4 import BeautifulSoup
import requests

response = requests.get('https://kabutan.jp/stock/kabuka?code=0000')
soup = BeautifulSoup(response.text, 'html.parser')
today_stock = soup.find('table', {'class': 'stock_kabuka0'}).find('tbody').find_all('td')
yesterday_stock = soup.find('table', {'class': 'stock_kabuka_dwm'}).find('tbody').find('tr').find_all('td')

today = {'open': today_stock[0].text, 'high':today_stock[1].text, 'low':today_stock[2].text, 'close':today_stock[3].text}
yesterday = {'open': yesterday_stock[0].text, 'high':yesterday_stock[1].text, 'low':yesterday_stock[2].text, 'close':yesterday_stock[3].text}
print(today)
print(yesterday)

def stock_data_scraping():
    print("scraping")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(stock_data_scraping, 'cron', hour=9, day_of_week='mon-fri', misfire_grace_time=300)# 毎日9時00分に実行
    scheduler.start()
