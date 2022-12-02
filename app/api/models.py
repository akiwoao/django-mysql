from django.db import models
from django.utils import timezone

# Create your models here.
class Stock(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'stocks'

class Price(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.now)
    open = models.DecimalField(max_digits=20, decimal_places=2)
    high = models.DecimalField(max_digits=20, decimal_places=2)
    low = models.DecimalField(max_digits=20, decimal_places=2)
    close = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.ForeignKey(Stock, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'prices'

class Predict(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=timezone.now)
    predict = models.DecimalField(max_digits=20, decimal_places=2)
    up_down = models.CharField(max_length=10)
    propriety = models.BooleanField(blank=True)
    stock = models.ForeignKey(Stock, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'predicts'
