from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import DataHistory, PotentialFranchise, Contact


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
        "id", "full_name", "email", "phone", "age", "city", "linkedin_link", "budget", "candidate_type", "score", "message", "created_at"
    )
    list_display_links = ["id", "full_name", "email"]
    list_filter = ("budget", "experience_auto", "projet")
    search_fields = ("full_name", "email", "phone", "city_for_franchise")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Main Info", {
            "fields": (
                "full_name", "email", "phone", "age", "city", "linkedin_link", "budget", "message", "score",
                "candidate_type", "formtype"
            )
        }),
        ("Motivation", {
            "fields": ("projet", "experience_auto", "experience_commerciale", "experience_entrepreneur",
                       "city_for_franchise", "engagement", "start_timing")
        }),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id", "full_name", "email", "telephone", "purpose", "message", "formtype", "created_at"
    )
    list_display_links = ["id", "full_name", "email"]
    list_filter = ("formtype",)
    search_fields = ("full_name", "email", "telephone")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Main Info", {
            "fields": (
                "full_name", "email", "telephone", "purpose", "message", "formtype"
            )
        }),
    )


# full_name = models.CharField(max_length=200, help_text='Nom complet *')
# email = models.EmailField(max_length=200, help_text='Adresse email *')
# telephone = models.CharField(max_length=200, help_text='Numéro de téléphone *')
# purpose = models.CharField(max_length=300)
# message = models.TextField(max_length=5000, blank=True)
# formtype = models.CharField(max_length=100)
