from django.db import models

class PRICES(models.Model):

    #id = models.AutoField(primary_key=True)
    #security_code = models.ForeignKey("test.stocks", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    open = models.DecimalField(max_digits=15, decimal_places=2)
    high = models.DecimalField(max_digits=15, decimal_places=2)
    low = models.DecimalField(max_digits=15, decimal_places=2)
    close = models.DecimalField(max_digits=15, decimal_places=2)
    predict_propriety = models.BooleanField()

# class STOCKS(models.Model):

#     id = models.AutoField(primary_key=True)
#     stock_name = models.CharField(max_length=20)
#     security_code = models.CharField(max_length=15)


# class PREDICT(models.Model):

#     id = models.AutoField(primary_key=True)
#     security_code = models.ForeignKey("test.stocks", on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now=False, auto_now_add=True)
#     predict_stock = models.DecimalField(max_digits=15, decimal_places=2)
#     up_down = models.BooleanField()
