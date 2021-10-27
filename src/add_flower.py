""" adds new flower in stock or adds flowers if user feels need to maintain stock for any flower """

from src.utility.constants import STOCK


class AddFlower:
    """
    has functions for adding new or in stock flowers
    """

    def __init__(self, flower_name: str):
        self.flower_name = flower_name.capitalize()

    def add_to_stock(self, valid_amount_to_add: int) -> list:
        """
        adds amount to stock
        :param valid_amount_to_add:
        :return: list of items in our stock
        """
        for item in STOCK:
            if item["flower_name"] == self.flower_name:
                item["quantity"] += valid_amount_to_add
        return STOCK

    def add_new_in_stock(self, valid_quantity: int, valid_price: float) -> list:
        """
        adds new flower if the flower name already exists then adds the quantity
        to stock meanwhile updates the value for price
        :param valid_quantity:
        :param valid_price:
        :return: list of items in our stock
        """
        exist = 0
        for item in STOCK:
            if self.flower_name == item["flower_name"]:
                item["quantity"] += valid_quantity
                item["price"] = valid_price
                exist += 1
                break
        if exist == 0:
            STOCK.append(
                {
                    "flower_name": self.flower_name,
                    "quantity": valid_quantity,
                    "price": valid_price,
                }
            )
        return STOCK
