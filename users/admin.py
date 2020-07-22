from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CreateUserForm
from .models import User, likebook

# class CustomUserAdmin(UserAdmin):
#     form = CreateUserForm

    

admin.site.register(User)
admin.site.register(likebook)
