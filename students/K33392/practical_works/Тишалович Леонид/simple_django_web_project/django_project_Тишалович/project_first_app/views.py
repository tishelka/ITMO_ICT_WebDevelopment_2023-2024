from django.shortcuts import render
from .models import CarOwner

def owner_detail(request, owner_id):
    owner = CarOwner.objects.get(id=owner_id)
    context = {'owner': owner}
    return render(request, 'owner_detail.html', context)
