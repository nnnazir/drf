from django.contrib import admin

from payments.models import Payment


@admin.register(Payment)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_of_payment', 'paid_lesson',
                    'paid_course', 'amount_payment', 'method_payment')
    list_filter = ('user', 'date_of_payment', 'paid_lesson',
                   'paid_course', 'amount_payment', 'method_payment')
    search_fields = ('user', 'date_of_payment', 'paid_lesson',
                     'paid_course', 'amount_payment', 'method_payment')
