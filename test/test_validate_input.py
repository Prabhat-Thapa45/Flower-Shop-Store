""" this module tests validate_input.py """

import pytest
from src.utility.validate_input import validate_float, validate_int


@pytest.fixture
def test_data():
    return [1, 3], [-1, "as", 0]


def test_validate_int(test_data):
    """ assert that valid int is returned """
    for i in test_data[0]:
        assert validate_int(i) == i


def test_validate_int_negative(test_data):
    """ assert that valid int was not passed """
    for i in test_data[1]:
        assert not validate_int(i)


def test_validate_float(test_data):
    """ assert that valid float is returned """
    for i in test_data[0]:
        assert validate_float(i) == i


def test_validate_float_negative(test_data):
    """ assert that valid float was not passed """
    for i in test_data[1]:
        assert not validate_float(i)
