from django.db import models

class CarOwner(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)

class DriverLicense(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateTimeField(null=True)

class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owners = models.ManyToManyField(CarOwner, through='Ownership')
