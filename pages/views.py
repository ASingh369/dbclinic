from django.shortcuts import render, redirect

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages, auth
from django.db.models import Count, Sum

from django.core.mail import send_mail

from pharmacy.models import Medicine, Order, Contact



def index(request):

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
    messages.success(request, 'Thank you for your message, a confirmation message has been sent to your email')

    return redirect('contact')
