"""
URL configuration for django_project_Тишалович project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from project_first_app import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('owners_list')), name='home'),
    path('owners/', views.list_owners, name='owners_list'),
    path('cars/', views.CarList.as_view(), name='cars_list'),
    path('cars/<int:car_id>/', views.CarDetail.as_view(), name='car_detail'),
    path('admin/', admin.site.urls),
    path('add_owner/', views.add_owner, name='add_owner'),
    path('car/add/', views.CarCreateView.as_view(), name='car_add'),
    path('car/<int:pk>/edit/', views.CarUpdateView.as_view(), name='car_edit'),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
]
