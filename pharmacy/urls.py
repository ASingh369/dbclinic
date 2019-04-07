from django.urls import path

from . import views

urlpatterns = [
    path('', views.pharmacy, name="pharmacy"),
    path('order_medicine', views.order_medicine, name="order_medicine"),
]
