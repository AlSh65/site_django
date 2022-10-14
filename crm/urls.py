from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]