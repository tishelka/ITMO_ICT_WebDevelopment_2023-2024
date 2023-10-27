from django.contrib import admin
from .models import CarOwner, DriverLicense, Ownership, Car

admin.site.register(CarOwner)
admin.site.register(DriverLicense)
admin.site.register(Ownership)
admin.site.register(Car)
