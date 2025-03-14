from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import DataHistory, PotentialFranchise


@admin.register(DataHistory)
class DataHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "id", "auto_mark", "auto_model", "auto_year", "auto_km",
        "firstname", "telephone", "email", "api_received", "formatted_features", "created_at"
    )
    list_display_links = ["id", "auto_mark"]
    list_filter = ("auto_mark", "auto_model", "auto_year", "api_received", "general_condition")
    search_fields = ("auto_mark", "auto_model", "email", "telephone", "code_postal")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("General", {
            "fields": ("auto_mark", "auto_model", "auto_year", "auto_km", "general_condition", "internal_state", "accident", "features", "api_data")
        }),
        ("Contact data", {
            "fields": ("firstname", "telephone", "email", "code_postal")
        }),
        ("API", {
            "fields": ("api_received", "formtype", "created_at")
        }),
    )

    def formatted_features(self, obj):
        try:
            return mark_safe(f"<ul>{''.join(f'<li>{feature}</li>' for feature in obj.features)}</ul>")
        except Exception:
            return obj.features

    formatted_features.short_description = "features"


@admin.register(PotentialFranchise)
class PotentialFranchiseAdmin(admin.ModelAdmin):
    list_display = (
        "id", "full_name", "email", "phone", "region", "experience", "budget", "message", "created_at"
    )
    list_display_links = ["id", "full_name"]
    list_filter = ("budget",)
    search_fields = ("full_name", "email", "phone", "region")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("General", {
            "fields": ("full_name", "email", "phone", "region", "experience", "budget", "message", "created_at")
        }),
    )
