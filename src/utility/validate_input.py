"""
This module validates int and float datatype and returns a valid int and float datatype
"""
from typing import Union


def validate_int(value) -> Union[int, bool]:
    """
    Returns positive int value else None
    :param value: str
    :return: int or None
    :raises: ValueError
    """
    try:
        value = int(value)
    except ValueError:
        return False
    else:
        if 1 <= value <= 200:
            return value
        return False


def validate_float(value) -> Union[float, None]:
    """
    Returns positive int value else None
    :param value: str
    :return: float or None
    :raises: ValueError
    """
    try:
        value = float(value)
    except ValueError:
        return False
    else:
        if value < 1:
            return False
        return value
