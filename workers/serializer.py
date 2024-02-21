from .models import *
from rest_framework import serializers

from .constants.default_values import DefaultValues
from .inspectors.data_validate_inspector import check_str, check_date


class EmployeeSerializer(serializers.ModelSerializer):
    full_name: str = serializers.CharField(
        min_length=DefaultValues.min_text_length.value,
        max_length=DefaultValues.max_text_length.value,
        validators=[check_str,]
    )

    birth_date: timezone = serializers.DateTimeField(
        validators=[check_date,]
    )

    class Meta:
        model = Employee
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    full_name: str = serializers.CharField(
        min_length=5,
        max_length=DefaultValues.max_text_length.value,
        validators=[check_str,]
    )

    birth_date: timezone = serializers.DateTimeField(
        validators=[check_date,]
    )

    class Meta:
        model = Client
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    name: str = serializers.CharField(
        min_length=DefaultValues.min_text_length.value,
        max_length=DefaultValues.max_text_length.value,
        validators=[check_str,]
    )

    price: float = serializers.FloatField(
        allow_null=False,
        validators=[check_price,],
    )

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    client: Client = ClientSerializer(
        required=True,
        allow_null=False,
    )

    product: Product = ProductSerializer(
        required=True,
        allow_null=False,
    )

    employee: Employee = EmployeeSerializer(
        required=True,
        allow_null=False,
    )

    price: float = serializers.FloatField(
        allow_null=False,
        validators=[check_price,]
    )

    date: timezone = serializers.DateTimeField(
        allow_null=False,
        validators=[check_date,],
    )

    class Meta:
        model = Order
        fields = '__all__'
