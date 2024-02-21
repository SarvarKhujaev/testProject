import typing

from cerberus import Validator

from django.utils import timezone
from .error_handler_inspector import ErrorInspector


ERROR: typing.Final[ErrorInspector] = ErrorInspector()
CHECK_NONE: typing.Final[typing.Callable] = lambda x: x is not None


def check_str(message: str):
    if message is None or len(message) < 3:
        ERROR.raise_error(message="param cannot be empty")


def check_price(price: float):
    if price > 0:
        ERROR.raise_error(message="temperature has to be in interval 34 to 42")


def compare_objects_identity(
    form: typing.Dict[str, typing.Any],  # принятая форма
    right_form: typing.Dict[str, typing.Any],  # то как она должна быть
    required_all: bool = True,
) -> tuple[bool, typing.Any]:  # правильная форма для сравнения
    validator: typing.Final[Validator] = Validator(
        required_all=required_all, allow_unknown=True
    )

    """
    возвращаем результат проверки и ошибку если есть
    """
    return validator.validate(form, right_form), validator.errors


def check_date(date: timezone):
    if date > timezone.now():
        ERROR.raise_error(message="Date cannot be from future")
