from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email')
    search_fields = ('username', 'email')
    fieldsets = (
        ('User Info', {
            'fields': ('username', 'email', 'password', 'first_name', 'last_name',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',
                       'is_email_verified','email_verification_token')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)