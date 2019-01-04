from django.db import models
from datetime import datetime

# medID, Name, Cost, Info, Quantity, medImage, medType

class Medicine(models.Model):
    medName = models.CharField(max_length=100)
    medInfo = models.TextField(blank=True)
    medType = models.CharField(max_length=200)
    medImage = models.ImageField(upload_to='photo/%Y/%m/%d/')
    medCost = models.DecimalField(max_digits=6, decimal_places=2)
    medQuantity = models.IntegerField(default=0)
    medDate = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.medName

