from django.db import models
from django.utils import timezone

# Create your models here.
class Stock(models.Model):
  id = models.CharField(max_length=12, primary_key=True)
  name = models.CharField(max_length=50)
  country = models.CharField(max_length=50)

class Price(models.Model):
  stock = models.ForeignKey(Stock, related_name='prices', on_delete=models.PROTECT)
  date = models.DateField(default=timezone.now)
  open = models.DecimalField(max_digits=20, decimal_places=2)
  high = models.DecimalField(max_digits=20, decimal_places=2)
  low = models.DecimalField(max_digits=20, decimal_places=2)
  close = models.DecimalField(max_digits=20, decimal_places=2)

class Predict(models.Model):
  stock = models.ForeignKey(Stock, related_name='predicts', on_delete=models.PROTECT)
  date = models.DateField(default=timezone.now)
  predict = models.DecimalField(max_digits=20, decimal_places=2)
  up_down = models.CharField(max_length=10)
  propriety = models.BooleanField()
