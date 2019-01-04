from django.db import models

class Doctor(models.Model):
    docName = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    docType = models.CharField(max_length=200)
    def __str__(self):
        return self.docName