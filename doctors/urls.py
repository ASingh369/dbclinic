from django.urls import path

from . import views

urlpatterns = [
    path('', views.doctors, name='doctors'),
    path('/<str:doctor_name>', views.doctor, name='doctor'),
    path('/doctor/book_appointment', views.book_appointment, name='book_appointment'),
]
