from django.shortcuts import render, redirect

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages, auth
from django.db.models import Count, Sum

from django.core.mail import send_mail

from pharmacy.models import Medicine, Order, Contact
from doctors.models import Schedule, Doctor, Appointment

from datetime import datetime, date, timedelta

import random


def index(request):
    update_schedules()

    # most sold medicines
    most_sold_medicines = Medicine.objects.annotate(items_sold=(Sum('order__quantity'))).order_by('-items_sold')

    # latest added medicines
    new_medicines = Medicine.objects.order_by('-medDate')[:3]

    context = {
        'newMedicines': new_medicines,
        'most_sold_medicines': most_sold_medicines,
    }

    return render(request, 'pages/index.html', context )


def contact(request):
    return render(request, 'pages/contact.html')

def send_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()

    # Send email
    send_mail(
        'DBClinic contact made',
        'Thank you for sending us a message, we will get back to you soon',
        'dbclinicteam@gmail.com',
        ['dbclinicteam@gmail.com', 'amritpalsinghs369@gmail.com', email],
        fail_silently=False
    )
    messages.success(request, 'Thank you for your time, a confirmation message has been sent to your email')

    return redirect('contact')


def update_schedules():
    # check if any schedule exits and get first shedule
    any_schedule = None
    any_schedule = Schedule.objects.all().first()
    if any_schedule:
        if (date.today() - any_schedule.appointment_date > timedelta(days=7)):
            # delete all appointments and schedules
            Appointment.objects.all().delete()
            Schedule.objects.all().delete()

            # add new schedule for each doctor
            all_doctors = Doctor.objects.filter()
            possible_times = ['08:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00']
            for single_doctor in all_doctors:
                for x in range(5):
                    schedule = Schedule(doctor=single_doctor, appointment_date=(date.today() + timedelta(days=1) + timedelta(days=x)), time=random.choice(possible_times))
                    schedule.save()

    else:
        # check if any doctor exists
        doctors = Doctor.objects.filter()
        if doctors:
            # add any old old time to schedule for first doctor
            schedule = Schedule(doctor=doctors[0], appointment_date=(date.today() - timedelta(days=10)), time="10:00-12:00")
            schedule.save()
            update_schedules()