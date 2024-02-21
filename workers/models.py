from django.db import models

from .inspectors.data_validate_inspector import *
from .constants.default_values import DefaultValues


class Employee(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True,
        auto_created=True,
    )

    full_name: str = models.CharField(
        max_length=DefaultValues.max_text_length.value,
        validators=[check_str],
        blank=False,
        null=False,
    )

    birth_date = models.DateField(
        blank=False,
        null=False,
    )

    class Meta:
        ordering: typing.List[str] = ["full_name"]


class Client(models.Model):
    id: models.AutoField = models.AutoField(
        primary_key=True,
        auto_created=True,
    )

    full_name: str = models.CharField(
        max_length=DefaultValues.max_text_length.value,
        validators=[check_str],
        blank=False,
        null=False,
    )

    birth_date = models.DateField(
        blank=False,
        null=False,
    )

    class Meta:
        ordering: typing.List[str] = ["full_name"]


class Product(models.Model):
    name: str = models.CharField(
        max_length=DefaultValues.max_text_length.value,
        validators=[check_str],
        blank=False,
        null=False,
    )

    price: float = models.FloatField(
        null=False,
        blank=False,
        validators=[check_price]
    )

    quantity: int = models.IntegerField(
        null=False,
        blank=False,
        default=0,
    )

    class Meta:
        ordering: typing.List[str] = ["name", "price"]


class Order(models.Model):
    client: Client = models.ForeignKey(
        to=Client,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    product: typing.List[Product] = models.ManyToManyField(
        to=Product,
        blank=False,
    )

    employee: Employee = models.ForeignKey(
        to=Employee,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    # общая цена заказа
    price: float = models.FloatField(
        null=False,
        blank=False,
    )

    date: timezone = models.DateTimeField(
        validators=[check_date],
        auto_now=True,
        editable=False,
    )

    class Meta:
        ordering: typing.List[str] = ["date", "price"]
