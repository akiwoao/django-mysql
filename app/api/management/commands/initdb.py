from django.core.management.base import BaseCommand
from api.models import TestOHLC
from datetime import datetime
from django.utils.timezone import make_aware
from decimal import *
from django.db import IntegrityError
import csv
import logging
logger = logging.getLogger(__name__)
import pandas as pd
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        # データベース全件削除
        TestOHLC.objects.all().delete()

        # csvファイルのデータをデータベースに保存
        with open("nikkei_kun.csv", encoding="utf-8") as f:
            reader = csv.reader(f)
            #next(reader)  # 先頭行を飛ばす
            for row in reader:
                ohlc = TestOHLC(
                    date=make_aware(datetime.strptime(row[0], '%Y/%m/%d')),
                    open=float(row[1]),
                    high=float(row[2]),
                    low=float(row[3]),
                    close=float(row[4]),
                )
                try:
                    ohlc.save()

                except IntegrityError:
                    logger.info("({date})既に登録されております".format(date=ohlc.date))
                    # 重複エラーが出た場合はfor文から抜ける
                    break
                except Exception as e:
                    logger.exception(e)
                    logger.error("({date})登録に失敗しました".format(date=ohlc.date))
