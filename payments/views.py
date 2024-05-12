from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from lms.permissions import IsOwnerOrStaff
from payments.services import create_stripe_price, create_stripe_session
from payments.models import Payment
from payments.serializers import PaymentSerializer
from users.permissions import IsModerator


class PaymentListView(generics.ListAPIView):
    """
    Класс для формирования списка платежей
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    search_fields = ['paid_lesson', 'paid_course', 'method_payment']
    ordering_fields = ('date_of_payment',)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('user', 'date_of_payment',
                        'paid_lesson', 'paid_course')
    filter_fields = ('user', 'date_of_payment',
                     'paid_lesson', 'paid_course')
    permission_classes = [IsOwnerOrStaff]


class PaymentCreateView(generics.CreateAPIView):
    """
    Класс для создания нового платежа
    """
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        course = serializer.validated_data.get('paid_course')
        if not course:
            raise serializers.ValidationError('Укажите курс')
        payment = serializer.save()
        stripe_price_id = create_stripe_price(payment)
        payment.payment_url, payment.payment_id = (
            create_stripe_session(stripe_price_id)
        )
        payment.save()


class PaymentDetailView(generics.RetrieveAPIView):
    """
    Класс для просмотра подробной информации по платежу
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all
    permission_classes = [IsOwnerOrStaff]


class PaymentUpdateView(generics.UpdateAPIView):
    """
    Класс для обновления данных по платежу
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all
    permission_classes = [IsOwnerOrStaff]


class PaymentDestroyView(generics.DestroyAPIView):
    """
    Класс для удаления платежа
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all
    permission_classes = [IsOwnerOrStaff]
