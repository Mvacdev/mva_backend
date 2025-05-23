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


class PotentialFranchise(TimeStampMixin, models.Model):
    # class AvailableBudget(models.TextChoices):
    #     # entre_20000_et_35000 = 'entre_20000_et_35000', 'Entre 20 000 € et 35 000 €'
    #     # _35000_et_50000 = '_35000_et_50000', '35 000 € et 50 000 €'
    #     # plus_de_50000 = 'plus_de_50000', 'Plus de 50 000 €'
    #     moins_20000 = 'moins_20000', 'Moins 20000'
    #     entre_20000_49000 = 'entre_20000_49000', 'Entre 20000-49000'
    #     plus_50000 = 'plus_50000', 'Plus 50000'
    full_name = models.CharField(max_length=200, help_text='Nom complet *')
    email = models.EmailField(max_length=200, help_text='Adresse email *')
    phone = models.CharField(max_length=200, help_text='Numéro de téléphone *')
    age = models.PositiveIntegerField(default=21)
    city = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=300, blank=True)
    message = models.TextField(max_length=5000, help_text='Message (facultatif)', blank=True)
    projet = models.CharField(max_length=100, help_text='Quel est votre projet ?')
    experience_auto = models.CharField(max_length=100, help_text='Avez-vous une expérience dans le secteur automobile ? *', blank=True, null=True)  # +
    experience_commerciale = models.CharField(max_length=100, help_text='Avez-vous une expérience commerciale ?')
    experience_entrepreneur = models.CharField(max_length=100, help_text='Êtes-vous déjà entrepreneur ou indépendant ?')
    city_for_franchise = models.CharField(max_length=100, help_text='Dans quelle ville/village souhaitez-vous vous implanter ? *')
    budget = models.CharField(max_length=100, help_text='Quelle est votre capacité d’investissement immédiate ?', blank=True, null=True)
    engagement = models.CharField(max_length=100, help_text='Êtes-vous prêt à vous engager à plein temps dans le projet ?')
    start_timing = models.CharField(max_length=100, help_text='Quand souhaitez-vous démarrer ?')
    score = models.PositiveIntegerField(default=0)
    candidate_type = models.CharField(max_length=100, help_text='Quand souhaitez-vous démarrer ?')
    formtype = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Potential franchise'
        verbose_name_plural = 'Potential franchises'
        ordering = ['-id']


class Contact(TimeStampMixin, models.Model):
    full_name = models.CharField(max_length=200, help_text='Nom complet *')
    email = models.EmailField(max_length=200, help_text='Adresse email *')
    telephone = models.CharField(max_length=200, help_text='Numéro de téléphone *')
    purpose = models.CharField(max_length=300)
    message = models.TextField(max_length=5000, blank=True)
    formtype = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-id']
