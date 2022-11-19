from django.contrib import admin

# Register your models here.
from .models import TestOHLC

class OHLCAdmin(admin.ModelAdmin):
    list_display = ('date', 'open', 'high', 'low', 'close')

admin.site.register(TestOHLC, OHLCAdmin)
