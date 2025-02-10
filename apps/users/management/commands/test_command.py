from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Закончили.')
