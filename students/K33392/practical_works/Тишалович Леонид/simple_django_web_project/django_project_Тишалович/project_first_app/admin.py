from django.contrib import admin
from .models import CarOwner, DriverLicense, Ownership, Car, UserProfile
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import UserProfile
from django.contrib.auth.models import User

admin.site.register(CarOwner)
admin.site.register(DriverLicense)
admin.site.register(Ownership)
admin.site.register(Car)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(DefaultUserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
