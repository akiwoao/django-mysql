from datetime import datetime, date
from beautifulsoup4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler

def stock_data_scraping():
    print("scraping")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(stock_data_scraping, 'cron', hour=9, day_of_week='mon-fri', misfire_grace_time=300)# 毎日9時00分に実行
    scheduler.start()
