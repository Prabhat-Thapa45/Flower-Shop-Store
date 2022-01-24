""" This module has test cases for static webpages
displayed in initial processes """


def test_index(welcome_client, welcome_urls):
    """ asserts valid response for get request """
    response = welcome_client.get(welcome_urls['index'])
    assert response.status_code == 200


def test_about(welcome_urls, welcome_client):
    """ asserts valid response for get request """
    response = welcome_client.get(welcome_urls['about'])
    assert response.status_code == 200


def test_contact(welcome_urls, welcome_client):
    """ asserts valid response for get request """
    response = welcome_client.get(welcome_urls['contact'])
    assert response.status_code == 200
