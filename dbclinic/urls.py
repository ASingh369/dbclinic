from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pharmacy.urls')),
    path('doctors/', include('doctors.urls')),
    path('admin/', admin.site.urls),
]
