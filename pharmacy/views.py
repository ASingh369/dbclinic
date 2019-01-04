from django.shortcuts import render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Medicine


def index(request):
    newMedicines = Medicine.objects.order_by('-medDate')[:3]

    context1 = {
        'newMedicines': newMedicines
    }

    return render(request, 'pages/index.html', context1 )


def about(request):
    return render(request, 'pages/about.html')


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