from django.contrib import admin

from .models import Medicine, Order, Contact

admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(Contact)