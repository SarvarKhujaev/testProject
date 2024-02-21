import typing
from workers.constants.default_values import DefaultValues


employee_model_json: typing.Dict[str, typing.Any] = {
    'full_name': {
        'type': 'string',
        'empty': False,
        'required': True,
        'maxlength': DefaultValues.max_text_length.value,
        'minlength': DefaultValues.min_text_length.value,
    },
}

product_model_json: typing.Dict[str, typing.Any] = {
    'name': {
        'type': 'string',
        'empty': False,
        'required': True,
        'maxlength': DefaultValues.max_text_length.value,
        'minlength': DefaultValues.min_text_length.value,
    },

    'price': {
        'min': 0,
        'empty': False,
        'required': True,
        'type': 'float',
    },
}

order_model_json: typing.Dict[str, typing.Any] = {
    'price': {
        'min': 0,
        'empty': False,
        'required': True,
        'type': 'float',
    },
}
