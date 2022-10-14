from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.http import Http404

from .forms import OrderForm
from .models import Order
from cms.models import Slider
from price.models import Card, Table


def main_page(request):
    slider = Slider.objects.all()
    card = Card.objects.all()
    table = Table.objects.all()
    form = OrderForm()
    dict_models = {
        'slider': slider,
        'card': card,
        'table': table,
        'form': form
    }
    return render(request, './index.html', dict_models)




class ThanksView(View):
    def post(self, request):
        if request.POST:
            name = request.POST['name']
            phone = request.POST['phone']
            element = Order(name=name, phone=phone).save()
            return render(request, 'thanks.html', {'name': name})
        else:
            return render(request, 'thanks.html')