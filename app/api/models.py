from django.db import models

# Create your models here.
class TestOHLC(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    open = models.DecimalField(max_digits=15, decimal_places=2)
    high = models.DecimalField(max_digits=15, decimal_places=2)
    low = models.DecimalField(max_digits=15, decimal_places=2)
    close = models.DecimalField(max_digits=15, decimal_places=2)
