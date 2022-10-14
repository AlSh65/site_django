from django.contrib import admin
from .models import Order, Comment, Status


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'status']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['status', ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'date', 'binding']
