from django.contrib import admin

# Register your models here.
from .models import Stock
from .models import Price
from .models import Predict

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
class PriceAdmin(admin.ModelAdmin):
    list_display = ('date', 'open', 'high', 'low', 'close')
class PredictAdmin(admin.ModelAdmin):
    list_display = ('date', 'predict', 'up_down', 'propriety')

admin.site.register(Stock, StockAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Predict, PredictAdmin)
