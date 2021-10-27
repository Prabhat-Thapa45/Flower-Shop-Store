""" this module tests add_flower_api """

import pytest
from src.utility.constants import STOCK


@pytest.fixture()
def invalid_data():
    return [(-1, 0, "str"), (("a", "sd"), (0, 0), (-1, 2))]


class TestGet:
    """ get request in add_flower.api """
    def test_add_flower(self, add_client, add_urls):
        """
        :param: add_client: client
        :param: add_urls: dict of urls for adding routes
        """
        url = add_urls['add_flower']
        response = add_client.get(url)
        assert response.status_code == 200

    def test_add_new_flower(self, add_client, add_urls):
        """
        :param: add_client: client
        :param: add_urls: dict of urls for adding routes
        """
        url = add_urls['add_new_flower']
        response = add_client.get(url)
        assert response.status_code == 200


class TestPost:
    def test_add_flower(self, add_client, add_urls):
        """ asserts if the page is redirected to correct page and quantity is updated
        :param: add_client: client
        :param: add_urls: dict of urls for adding routes"""
        url = add_urls['add_flower']
        assert STOCK[0]['quantity'] == 20
        response = add_client.post(url, data={'number': 4, 'flower_name': 'Rose'})
        # redirect is done to refresh the page so status code is 302
        assert response.status_code == 302
        assert response.request.path == url
        assert STOCK[0]['quantity'] == 24

    def test_add_flower_negative(self, add_client, add_urls, invalid_data):
        """ asserts that the invalid data are not added rather rejected
        :param: add_client: client
        :param: add_urls: dict of urls for adding routes
        :raise: TypeError: while adding int with str
        """
        url = add_urls['add_flower']
        for i in invalid_data[0]:
            response = add_client.post(url, data={'number': i, 'flower_name': 'Rose'})
            assert response.status_code == 302
            try:
                assert STOCK[0]['quantity'] != 20 + i
            except TypeError:
                pass

    def test_add_new_flower(self, add_client, add_urls):
        """
        asserts if the new flower is added or not
        :param: add_client: client
        :param: add_urls: dict of urls for adding routes
        :return:
        """
        url = add_urls['add_new_flower']
        assert len(STOCK) == 2
        response = add_client.post(url, data={'flower_name': 'Orchid', 'quantity': '20', 'price': '4.5'})
        assert response.status_code == 302
        assert STOCK[-1] == {'flower_name': 'Orchid', 'quantity': 20, 'price': 4.5}
        assert len(STOCK) == 3

    def test_add_new_flower_negative(self, add_client, add_urls, invalid_data):
        """
        asserts that no new data is added
        :param: add_client: client
        :param: add_urls: dict of urls for adding routes
        :param invalid_data: from above fixture
        :return:
        """
        url = add_urls['add_new_flower']
        length = len(STOCK)
        for i, j in invalid_data[1]:
            response = add_client.post(url, data={'flower_name': 'Orchid', 'quantity': i, 'price': j})
            assert response.status_code == 200
            # shows that no new items are added
            assert len(STOCK) == length
