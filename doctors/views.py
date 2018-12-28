from django.shortcuts import render

from django.http import HttpResponse


def doctors(request):
    return render(request, 'doctor/doctors.html')
