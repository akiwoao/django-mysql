from django.db import models

# Create your models here.
class Stock(models.Model):
  id = models.CharField(max_length=12, primary_key=True)
  name = models.CharField(max_length=50)
  country = models.CharField(max_length=50)

class Price(models.Model):
  stock = models.ForeignKey(Stock, on_delete=models.PROTECT, to_field="id")
  date = models.DateTimeField(auto_now=False, auto_now_add=False)
  open = models.DecimalField(max_digits=20, decimal_places=2)
  high = models.DecimalField(max_digits=20, decimal_places=2)
  low = models.DecimalField(max_digits=20, decimal_places=2)
  close = models.DecimalField(max_digits=20, decimal_places=2)

class Predict(models.Model):
  stock = models.ForeignKey(Stock, on_delete=models.PROTECT, to_field="id")
  date = models.DateTimeField(auto_now=False, auto_now_add=False)
  predict = models.DecimalField(max_digits=20, decimal_places=2)
  UP_DOWN_CHOICES = (
        (True, '上昇'),
        (False, '下降'),
    )
  up_down = models.BooleanField(choices=UP_DOWN_CHOICES)
  propriety = models.BooleanField()
