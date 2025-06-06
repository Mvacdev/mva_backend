import os
from urllib.parse import urljoin

from django.core.files.storage import FileSystemStorage

from mva_proj import settings


class CustomStorage(FileSystemStorage):
    """Custom storage for django_ckeditor_5 images."""

    location = os.path.join(settings.MEDIA_ROOT, "django_ckeditor_5")
    base_url = '/' + urljoin(settings.MEDIA_URL, "django_ckeditor_5/")
