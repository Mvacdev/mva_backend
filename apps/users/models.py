from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group

from django.db import models
from django.utils import timezone

from mva_proj import defs


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_active, is_staff, is_superuser, **extra_fields):
        # if not username:
        #     raise TypeError('Users must have a username.')
        extra_fields.pop('first_name', None)
        extra_fields.pop('last_name', None)

        email = self.normalize_email(email)
        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser,
            date_joined=timezone.now(), **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(
            email, password, is_active=True, is_staff=False, is_superuser=False, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(
            email, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # def get_upload_picture(self, instance):
    #     basename = str(uuid.uuid4())
    #     discard, ext = os.path.splitext(instance)
    #     return f'users/{self.id}/profile_pictures/{"".join([basename, ext])}'

    username = models.CharField(max_length=defs.NAME_LENGTH, null=True, blank=True, verbose_name='Username')
    # profile_picture = models.ImageField(upload_to=get_upload_picture, default=None, verbose_name='Фото профиля', null=True, blank=True)

    email = models.EmailField(max_length=defs.NAME_LENGTH, unique=True, verbose_name='Email')
    email_verified = models.BooleanField(default=False, verbose_name='Email confirmed')

    groups = models.ManyToManyField(to=Group, blank=True, verbose_name='Groups')

    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_staff = models.BooleanField(default=False, verbose_name='Stuff')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser')

    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Date joined')

    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Updated at')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS = ['email']

    @property
    def name(self):
        if self.username:
            return f"{self.username}"
        # if self.first_name:
        #     return f'{self.first_name or ""} {self.last_name or ""}'.strip()
        else:
            return f"{self.email}"

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)

        if self.id:
            self.updated_at = timezone.now()

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

