# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import CustomUser




@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['username','last_name','first_name','is_superuser','is_staff','is_active','last_login','date_joined']
    list_filter = ('is_staff','is_superuser',)
    
    # fieldsets for modifying user
    fieldsets = (
        (None,              {'fields': ('title','first_name','last_name', 'password')}),
        ('Contact info',    {'fields': ('email',)}),
        ('About', {'fields': ('bio','image','image_tag')}),
        ('Address',         {'fields': ('address1','address2','address3','postcode','city','state','country',)}),
        ('Permissions',     {'fields': ('is_active','is_staff','groups','user_permissions')}),
    )

    # fieldsets for creating new user
    add_fieldsets = (
        (None,    {'fields': (('image','image_tag'),'last_name','first_name','email', 'password1', 'password2')}),
        # ('Address',         {'fields': ('university','address1','address2','city','state','country',)}),
    )

    search_fields = ('email',)
    ordering = ('last_name',)
    # filter_horizontal = ()
    readonly_fields = ['image_tag',]
