from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('pharmacy', views.pharmacy, name="pharmacy"),
    path('order_medicine', views.order_medicine, name="order_medicine"),
]
