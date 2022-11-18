from django.core.management.base import BaseCommand
from django.conf import settings
from test.models import PRICES
import csv
import glob
import os
import datetime
from django.db import IntegrityError
import logging
logger = logging.getLogger(__name__)
import pandas as pd
import random
from decimal import *
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.generate_price_from_csv_file()


    def generate_price_from_csv_file(self):
        with open("nikkei_kun.csv", encoding="utf-8") as f:
            reader = csv.reader(f)
            #next(reader)  # 先頭行を飛ばす
            for row in reader:
                prices = PRICES(
                    date=datetime.strptime(row[0], '%Y/%m/%d').date(),
                    open=float(row[1]),
                    high=float(row[2]),
                    low=float(row[3]),
                    close=float(row[4]),
                    predict_propriety=bool(random.choice([True, False]))
                )
                try:
                    prices.save()

                except IntegrityError:
                    logger.info("({date})既に登録されております".format(date=prices.date))
                    # 重複エラーが出た場合はfor文から抜ける
                    break
                except Exception as e:
                    logger.exception(e)
                    logger.error("({date})登録に失敗しました".format(date=prices.date))
