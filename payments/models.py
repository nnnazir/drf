from django.db import models
from django.db.models import CASCADE

from lms.models import Lesson, Course
from users.models import NULLABLE, User


class Payment(models.Model):
    """
    Модель платежей:
    пользователь,
    дата оплаты,
    оплаченный курс или урок,
    сумма оплаты,
    способ оплаты: наличные или перевод на счет.
    """
    PAYMENT_CHOICE = [
        ('cash', 'наличными'),
        ('card', 'картой'),
    ]
    user = models.ForeignKey(User, on_delete=CASCADE,
                             verbose_name='пользователь',
                             related_name='payment')
    date_of_payment = models.DateField(verbose_name='дата платежа')
    paid_lesson = models.ForeignKey(Lesson, on_delete=CASCADE, **NULLABLE,
                                    verbose_name='оплаченный урок',
                                    related_name='lessons')
    paid_course = models.ForeignKey(Course, on_delete=CASCADE, **NULLABLE,
                                    verbose_name='оплаченный курс',
                                    related_name='courses')
    amount_payment = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name='сумма оплаты')
    method_payment = models.CharField(max_length=10, choices=PAYMENT_CHOICE,
                                      verbose_name='метод оплаты')
    payment_url = models.URLField(max_length=400, **NULLABLE,
                                  verbose_name='ссылка на оплату')
    payment_id = models.CharField(max_length=100, **NULLABLE,
                                  verbose_name='идентификатор платежа')

    def __str__(self):
        return f'{self.user} оплатил {self.date_of_payment}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
