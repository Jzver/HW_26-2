from rest_framework import serializers

from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    payment_history = PaymentSerializer(source="payment_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"