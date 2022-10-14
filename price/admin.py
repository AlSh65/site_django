from django.contrib import admin

from .models import Card, Table


@admin.register(Card)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['value', 'description', ]

@admin.register(Table)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'old_price', 'new_price']
