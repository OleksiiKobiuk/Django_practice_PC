from django.contrib import admin

from .models import ComputerModel

@admin.register(ComputerModel)
class CompAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'ram', 'processor', 'monitor')
