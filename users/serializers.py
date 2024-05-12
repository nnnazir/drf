from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

from payments.serializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя
    """
    history_payment = PaymentSerializer(many=True, read_only=True,
                                        source='payment')

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'phone',
            'avatar',
            'city',
            'history_payment',
            'is_staff',
            'is_active'
        ]

    def get_history_payment(self, instance):
        return instance.history_payment


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        token = super().get_token(user)
        token['email'] = user.email
        return token
