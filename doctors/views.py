from django.shortcuts import render

from .models import Doctor


def doctors(request):
    doctors = Doctor.objects.all()

    context = {
        'doctors': doctors
    }
    return render(request, 'doctor/doctors.html', context)
