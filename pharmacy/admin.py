from django.contrib import admin

from .models import Medicine, Order, Contact

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'medName', 'medType', 'medCost', 'medQuantity', 'medDate')
    list_display_links = ('id', 'medName')
    list_filter = ('medType',)
    search_fields = ('medName', 'medInfo')
    list_per_page = 10

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'medicine', 'name', 'email', 'quantity', 'order_date')
    list_display_links = ('id', 'medicine')
    list_filter = ('quantity', )
    search_fields = ('medicine', 'name', 'email', 'quantity')
    list_per_page = 10

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'message', 'email')
    list_per_page = 10

admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Contact, ContactAdmin)