from django.db import models
from django.utils import timezone


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    # @property
    # def created(self):
    #     return get_local_formatted_datetime(self.created_at)

    # @property
    # def updated(self):
    #     return get_local_formatted_datetime(self.updated_at)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        try:
            if getattr(self, 'id'):
                self.updated_at = timezone.now()
        except AttributeError:
            pass
        super().save(*args, **kwargs)
