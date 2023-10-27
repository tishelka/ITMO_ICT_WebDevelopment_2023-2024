from django import forms
from .models import CarOwner, Car
from .models import UserProfile

class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ['name', 'surname', 'birth_date']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['license_plate', 'brand', 'model', 'color']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['passport_number', 'home_address', 'nationality']