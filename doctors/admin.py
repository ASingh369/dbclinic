from django.contrib import admin

from .models import Doctor, Schedule, Appointment

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'docName', 'docType', 'email')
    list_display_links = ('id', 'docName')
    list_filter = ('docType',)
    search_fields = ('docName', 'docType', 'email')
    list_per_page = 10

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'schedule')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user')
    list_per_page = 10

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'appointment_date', 'time', 'booked')
    list_display_links = ('id', 'doctor')
    list_filter = ('booked', 'doctor', 'appointment_date')
    search_fields = ('doctor', 'appointment_date')
    list_per_page = 20

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Schedule, ScheduleAdmin)
