""" this module tests order.py """

from src.order import Order, cancel
from src.utility.constants import BQ_SIZE, YOUR_CART, STOCK


def test_cancel():
    """
    clears items from your cart
    """
    cancel()
    assert YOUR_CART == []


class TestOrders:
    """ has test cases for post requests in order.py """
    def test_flower_out_of_stock(self, order):
        """ Asserts two situation first in stock and second out of stock
        :param order: tuple of two objects of class Order
        """
        # In stock = 10, ordered quantity = 4
        assert not order[0].flower_out_of_stock()
        # Here in stock = 3, ordered quantity = 4
        assert order[1].flower_out_of_stock()

    def test_bq_size_exceeded(self, order):
        """
        asserts if ordered flower doesn't exceeds BQ_SIZE limit
        :param order: tuple of two objects of class Order
        """
        # BQ_SIZE = 4, order quantity = 4
        BQ_SIZE[0] = 4
        assert not order[0].bq_size_exceeded()

    def test_bq_size_exceeded_negative(self, order):
        """
        assert that bouquet size is exceeded
        :param order: tuple of two objects of class Order.
        :return:
        """
        # BQ_SIZE = 2, order quantity = 4
        BQ_SIZE[0] = 2
        assert order[0].bq_size_exceeded()

    def test_adding_to_cart(self, order):
        """
        asserts if item is added to your cart and BQ_SIZE is also reduced
        :param order: tuple of two objects of class Order.
        :return:
        """
        BQ_SIZE[0] = 4
        assert len(order[0].adding_to_cart()) == 1
        # ordered quantity is 4 so BQ_SIZE got reduced by 4
        assert BQ_SIZE[0] == 0
        YOUR_CART.clear()

    def test_check_order_criteria(self):
        """ asserts true only if BQ_SIZE == 0 """
        BQ_SIZE[0] = 0
        assert Order.check_order_criteria()
        BQ_SIZE[0] = 1
        assert not Order.check_order_criteria()

    def test_proceed_to_buy(self, order):
        """
        Reduces quantity from stock and clears items from your cart
        :param order: tuple of two objects of class Order
        """
        # initialised 20 in stock for Rose
        STOCK[0]['quantity'] = 20
        # added 4 flowers from first element in STOCK i.e. ROSE to cart
        order[0].adding_to_cart()
        # called the function
        Order.proceed_to_buy()
        assert STOCK[0]['quantity'] == 16
        assert YOUR_CART == []
