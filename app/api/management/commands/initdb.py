from django.core.management.base import BaseCommand
from api.models import Price,Predict,Stock
from datetime import datetime
from django.utils.timezone import make_aware
from decimal import *
from django.db import IntegrityError
import csv
import logging
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        # データベース全件削除
        Price.objects.all().delete()
        Predict.objects.all().delete()
        Stock.objects.all().delete()

        # Stock テーブルに株価情報保存
        Stock(id="0000", name="日経平均株価", country="japan").save()
        stock = Stock.objects.get(id="0000")

        # csvファイルのデータをデータベースに保存
        with open("nikkei_kun.csv", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                price = stock.price_set.create(
                    stock = Stock.id,
                    date = make_aware(datetime.strptime(row[0], '%Y/%m/%d')),
                    open = float(row[1]),
                    high = float(row[2]),
                    low = float(row[3]),
                    close = float(row[4]),
                )
                predict = stock.predict_set.create(
                    stock = Stock.id,
                    date = make_aware(datetime.strptime(row[0], '%Y/%m/%d')),
                    predict = float(row[1]) - 5,
                    up_down = "up",
                    propriety = True
                )
                try:
                    price.save()
                    predict.save()

                except IntegrityError:
                    logger.info("({date})既に登録されております".format(date=price.date))
                    # 重複エラーが出た場合はfor文から抜ける
                    break
                except Exception as e:
                    logger.exception(e)
                    logger.error("({date})登録に失敗しました".format(date=price.date))
