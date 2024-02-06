from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='نام')
    last_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='نام خانوادگی')
    username = models.CharField(
        unique=True, max_length=255, null=False, blank=False, verbose_name='نام کاربری')
    phone_number = models.CharField(
        unique=True, max_length=14, verbose_name='تلفن همراه')
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    profile_image = models.ImageField(
        upload_to='images/profiles', verbose_name='پروفایل', null=False, blank=True,
        default='images/profiles/default_profile.png')

    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['id', 'last_name', 'first_name']
