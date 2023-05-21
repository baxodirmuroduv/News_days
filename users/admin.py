from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeFrom
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeFrom
    model = CustomUser
    list_display = ['email', 'username', 'age', 'address', 'job']


admin.site.register(CustomUser, CustomUserAdmin)
