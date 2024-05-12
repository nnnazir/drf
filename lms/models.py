"""
Файл с описанием моделей по курсу обучения и урокам.
"""
from django.db import models

from users.models import User, NULLABLE


class Course(models.Model):
    """
    Модель курса обучения
    """

    name = models.CharField(max_length=100, verbose_name='наименование')
    preview = models.ImageField(upload_to='course_previews/',
                                verbose_name='картинка',
                                **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='владелец', related_name='course')
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """
    Модель урока курса обучения
    """

    name = models.CharField(max_length=100, verbose_name='название урока')
    preview = models.ImageField(upload_to='lesson_previews/',
                                verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_url = models.URLField(verbose_name='видеоурок', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name='курс',
                               related_name='lessons')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='владелец', related_name='lesson')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('name', 'course',)


class Subscription(models.Model):
    """
    Модель подписки на курс
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='владелец',
                              related_name='subscription')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE,
                               verbose_name='курс',
                               related_name='subscriptions')
    status = models.BooleanField(default=False, verbose_name='статус подписки',
                                 **NULLABLE)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.owner}: {self.course}'
