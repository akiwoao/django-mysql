from django.contrib import admin

# Register your models here.
from .models import PRICES

# admin.site.register(User)

class RawPricesAdmin(admin.ModelAdmin):
    list_display = ('date', 'open', 'high', 'low', 'close', 'predict_propriety')

admin.site.register(PRICES, RawPricesAdmin)
