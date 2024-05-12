from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """
    Класс, описывающий модель пользователь
    Стандартная модель расширяется:
    avatar - «Аватар»,
    phone - «Номер телефона»,
    country - «Страна».
    Авторизация меняется на email
    role - обычный пользователь или модератор
    """
    username = None
    email = models.EmailField(max_length=200, verbose_name='электронная почта',
                              unique=True)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар',
                               **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices,
                            default=UserRoles.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
