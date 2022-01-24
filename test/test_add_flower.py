""" this module tests add_flower.py """

from src.utility.constants import STOCK
from src.utility.validate_input import validate_float, validate_int


def test_add_to_stock(add):
    """ assert if the stocks are added """
    assert STOCK[0]['quantity'] == 20
    add[0].add_to_stock(10)
    assert STOCK[0]['quantity'] == 30
    STOCK[0]['quantity'] = 20


def test_add_to_stock_negative(add):
    """ assert if the stocks are added """
    assert STOCK[0]['quantity'] == 20
    for i in ["2.32", "sd", -2, 0, 201]:
        value = validate_int(i)
        add[0].add_to_stock(value)
        # there is no change in our stock on invalid input
        assert STOCK[0]['quantity'] == 20
    STOCK[0]['quantity'] = 20


def test_add_new_in_stock(add):
    """ asserts if new items is added or not and also the correct value is added
    :param: add: it's a tuple of two objects of AddFlower, where add[0] = AddFLower("Sunflower")
    """
    length = len(STOCK)
    # here first parameter is for quantity and second for price while flower name is initialised already
    add[1].add_new_in_stock(10, 4.5)
    assert len(STOCK) == length + 1
    assert STOCK[-1] == {'flower_name': "Sunflower", 'quantity': 10, "price": 4.5}
    STOCK.pop()


def test_add_new_in_stock_negative(add):
    """ asserts if new items is added or not and also the correct value is added
    :param: add: it's a tuple of two objects of AddFlower, where add[0] = AddFLower("Sunflower")
    """
    length = len(STOCK)
    # here first parameter is for quantity and second for price while flower name is initialised already
    for i in [(0, 1.1), ("we", "EW"), (0, 0)]:
        add[1].add_new_in_stock(10, 4.5)
    assert not STOCK[-1] == {'flower_name': "Sunflower", 'quantity': 10, "price": 4.5}
    STOCK.pop()
