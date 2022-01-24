""" this module tests order_api.py """

from src.utility.constants import BQ_SIZE, YOUR_CART


def test_get_bouquet_size(order_client, order_urls):
    """
    :param: order_client: client for order_api.py
    :param: order_urls: dict of routes in order_api.py
    """
    url = order_urls['bouquet_size']

    response = order_client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


class TestPost:
    """ test methods for post request on order_api.py """

    def test_bouquet_size(self, order_client, order_urls):
        """
        asserts status code and BQ_SIZE for each input
        :param: order_client: client for order_api.py
        :param: order_urls: dict of routes in order_api.py
        """
        url = order_urls['bouquet_size']
        for i in [1, 3, 6]:
            response = order_client.post(url, data={'bouquet_size': i})
            assert response.status_code == 200
            assert response.request.path == url
            assert BQ_SIZE == [i]

    def test_bouquet_size_negative(self, order_client, order_urls):
        """
        asserts BQ_SIZE for invalid input is not accepted
        :param: order_client: client for order_api.py
        :param: order_urls: dict of routes in order_api.py
        """
        url = order_urls['bouquet_size']
        BQ_SIZE[0] = 0
        for i in [0, -1, 'w']:
            response = order_client.post(url, data={'bouquet_size': i})
            assert response.status_code == 200
            assert response.request.path == url
            assert BQ_SIZE[0] == 0

    def test_add_to_cart(self, order_client, order_urls, order):
        """
        asserts that the valid data is passed in post request
        :param: order_client: client for order_api.py
        :param: order_urls: dict of routes in order_api.py
        """
        url = order_urls['add_to_cart']
        response = order_client.post(url, data={'number': 2, 'flower_name': 'Rose', 'price': 2.20, 'in_stock': 10})
        assert response.status_code == 200

    def test_add_to_cart_negative(self, order_client, order_urls):
        """
        asserts that invalid data passed are rejected and same page is rendered with 400 status code
        :param: order_client: client for order_api.py
        :param: order_urls: dict of routes in order_api.py
        """
        url = order_urls['add_to_cart']
        # giving bouquet size of 4
        order_client.post(url, data={'bouquet_size': 4})
        for i in ['h', -2]:
            response = order_client.post(url, data={'number': i, 'flower_name': 'Rose', 'price': 2.20, 'in_stock': 10})
            assert response.status_code == 400
            assert response.request.path == url

    def test_go_to_cart(self, order_client, order_urls):
        """
        asserts if the requested post method is allowed
        :param: order_client: client for order_api.py
        :param: order_urls: dict of routes in order_api.py
        """
        url = order_urls['got_to_cart']
        response = order_client.post(url)
        assert response.status_code == 200
        assert response.request.path == url

    def test_cancel_order(self, order_client, order_urls):
        """
        asserts if items in your cart is cleared and valid page is rendered
        :param: order_client: client for order_api.py
        :param: order_urls: dict of routes in order_api.py
        """
        url = order_urls['cancel']
        response = order_client.post(url)
        assert response.status_code == 200
        assert len(YOUR_CART) == 0
        assert response.request.path == url

    def test_buy(self, order_client, order_urls):
        """
        asserts valid response to post request
        :param: order_client: client for order_api.py
        :param: order_urls: dict of routes in order_api.py
        """
        url = order_urls['buy']
        response = order_client.post(url)
        assert response.status_code == 200
        assert response.request.path == url
