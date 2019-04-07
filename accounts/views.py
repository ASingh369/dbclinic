from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from pharmacy.models import Order
from doctors.models import Appointment, Schedule
from datetime import datetime

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register') 
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register') 
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')

    # user's appointments
    user_appointments = Appointment.objects.filter(user=request.user, schedule__appointment_date__gt=datetime.now()).order_by('-schedule__appointment_date')

    
    # user orders
    user_orders = Order.objects.filter(user_id=request.user.id).order_by('-order_date')

    context = {
        'user_orders': user_orders,
        'user_appointments': user_appointments,
    }

    return render(request, 'accounts/dashboard.html', context)

def cancel_appointment(request):
    if request.method == 'POST':
        appointment_id = int(request.POST['appointment_id'])
        appointment = Appointment.objects.get(id=appointment_id)
        schedule = Schedule.objects.get(id=appointment.schedule.id)

        appointment.delete()
        schedule.booked = False

        schedule.save()
        messages.success(request, 'Your appointment was canceled successfully')

    return redirect('dashboard')