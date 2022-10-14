from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'get_image']


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url}>')
