from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django_json_widget.widgets import JSONEditorWidget

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    list_display = [
        'id', 'email', 'username', 'date_joined', 'last_login', 'is_superuser', 'email_verified'
    ]
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'email_verified']
    list_display_links = ['email', 'username']
    date_hierarchy = 'date_joined'
    search_fields = ('email', 'username')
    readonly_fields = ['last_login', 'date_joined']
    # readonly_fields = []
    fieldsets = (
        (None, {'fields': ('email', 'password', 'email_verified')}),
        (_('Personal info'), {'fields': ('username',)}),
        (_('Rights'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
