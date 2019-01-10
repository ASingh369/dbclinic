from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Doctor, Schedule, Appointment
from django.contrib.auth.models import User

def doctors(request):
    doctors = Doctor.objects.all()

    context = {
        'doctors': doctors
    }
    return render(request, 'doctor/doctors.html', context)


def doctor(request, doctor_name):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        schedule_id = request.POST['schedule_id']
        schedule = Schedule.objects.get(id=schedule_id)
        if schedule.booked:
            messages.error(request, 'Appointment already booked')
        else:
            user = User.objects.get(id=user_id)
            appointment = Appointment(schedule=schedule, user=user)
            appointment.save()
            schedule.booked = True
            schedule.save()
            messages.success(request, 'Your appointment have been booked successfully')
            
    doctor = get_object_or_404(Doctor, docName=doctor_name)
    schedule = Schedule.objects.filter(doctor=doctor.id)
    context = {
        'doctor': doctor,
        'schedule': schedule
    }
    return render(request, 'doctor/doctor.html', context)
