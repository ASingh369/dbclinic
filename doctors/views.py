from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Doctor, Schedule, Appointment
from django.contrib.auth.models import User
from pages.views import update_schedules
from datetime import datetime, date, timedelta

def doctors(request):
    update_schedules()

    doctors = Doctor.objects.all()

    context = {
        'doctors': doctors
    }
    return render(request, 'doctor/doctors.html', context)

def book_appointment(request):
    print("please be here")
    if request.method == 'POST':
        user_id = request.POST['user_id']
        schedule_id = request.POST['schedule_id']
        doc_name = request.POST['doc_name']
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
    return redirect('doctor', doc_name)


def doctor(request, doctor_name):
    update_schedules()

    doctor = get_object_or_404(Doctor, docName=doctor_name)

    schedule = Schedule.objects.filter(doctor=doctor.id).order_by('appointment_date')

    # booked missed appointments
    for single_schedule in schedule:
        if single_schedule.appointment_date <= date.today():
            single_schedule.booked = True
            single_schedule.save()

    context = {
        'doctor': doctor,
        'schedule': schedule
    }
    return render(request, 'doctor/doctor.html', context)
