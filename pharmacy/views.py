from django.shortcuts import render, redirect

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages, auth

from .models import Medicine, Order


def index(request):
    newMedicines = Medicine.objects.order_by('-medDate')[:3]

    context1 = {
        'newMedicines': newMedicines
    }

    return render(request, 'pages/index.html', context1 )


def about(request):
    return render(request, 'pages/about.html')

def order_medicine(request):
    if request.method == 'POST':
        med_id = request.POST['med_id']
        name = request.POST['name']
        email = request.POST['email']
        quantity = int(request.POST['quantity'])
        user_id = request.POST['user_id']

        medicine = Medicine.objects.get(id=med_id)

        medicine.medQuantity = medicine.medQuantity - quantity
        medicine.save()
        
        order = Order(medicine=medicine, name=name, email=email, quantity=quantity, user_id=user_id)

        order.save()
        messages.success(request, 'Your order was placed successfully! You can pick it up whenever you visit our clinic')

    return redirect('pharmacy')

def pharmacy(request):
    # All Medicines 
    queryset_list = Medicine.objects.order_by('medName')

    # filter by keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(medInfo__icontains=keywords)

    # filter by Name
    if 'medName' in request.GET:
        medName = request.GET['medName']
        if medName:
            queryset_list = queryset_list.filter(medName__icontains=medName)

    # filter by Max Price
    if 'maxPrice' in request.GET:
        price = request.GET['maxPrice']
        if price:
            queryset_list = queryset_list.filter(medCost__lte=price)

    

    context = {
        'medicines': queryset_list,
        'value': request.GET
    }

    return render(request, 'pages/pharmacy.html', context)