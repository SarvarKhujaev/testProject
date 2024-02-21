from enum import Enum


class DefaultValues(Enum):
    default_age: int = 18
    default_value: int = 0
    default_rating: int = 5.0
    default_duration: int = 120
    default_description: str = 'just some video'

    default = 'NOT NULL DEFAULT'
    not_null = 'NOT NULL'

    min_text_length: int = 3
    max_text_length: int = 200
