import os

import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import TextChoices
from django.utils.text import slugify
from slugify import slugify

from mva_proj.shared_mixins import TimeStampMixin


def custom_slugify(value):
    return slugify(value, separator='-')


class DataHistory(TimeStampMixin, models.Model):
    auto_mark = models.CharField(max_length=50)
    auto_model = models.CharField(max_length=50)
    auto_year = models.PositiveIntegerField()
    auto_km = models.PositiveIntegerField()
    general_condition = models.CharField(max_length=50)
    internal_state = models.CharField(max_length=50)
    accident = models.CharField(max_length=50)
    features = models.JSONField(blank=True, null=True, default=None)
    firstname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)  # Можно сделать PhoneNumberField (django-phonenumber-field)
    email = models.EmailField()
    code_postal = models.CharField(max_length=10)
    api_received = models.BooleanField(default=False)
    formtype = models.CharField(max_length=50)
    api_data = models.JSONField(blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.auto_mark} {self.auto_model} ({self.auto_year}) - {self.firstname}"

    class Meta:
        verbose_name = 'DataHistory'
        verbose_name_plural = 'DataHistories'
        ordering = ['-id']
        # constraints = [
        #     UniqueConstraint(
        #         fields=['user', 'code'],
        #         condition=Q(deleted=False),
        #         name='unique_product_user_code'
        #     )
        # ]
