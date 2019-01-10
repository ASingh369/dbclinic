from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Doctor(models.Model):
    docName = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    docType = models.CharField(max_length=200)
    def __str__(self):
        return self.docName

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    appointment_date = models.DateField()
    time = models.CharField(max_length=100)
    booked = models.BooleanField(default=False)
    def __str__(self):
        return self.time

class Appointment(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # def __str__(self):
    #     return self.id


