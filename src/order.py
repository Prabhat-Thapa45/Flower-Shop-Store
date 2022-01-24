""" has all the functionalities to make order for """

from typing import Union

from src.utility.constants import BQ_SIZE, STOCK, YOUR_CART


def cancel() -> None:
    """clears data from your cart"""
    YOUR_CART.clear()


class Order:
    """
    Helps in taking order
    """

    def __init__(self, valid_order_quantity, in_stock, flower_name, price):
        self.valid_order_quantity = valid_order_quantity
        self.in_stock = in_stock
        self.flower_name = flower_name
        self.price = price

    def flower_out_of_stock(self) -> Union[bool, None]:
        """
        Checks if flower is in stock or not
        :return: True if out of stock else None
        """
        if len(YOUR_CART) > 0:
            for item in YOUR_CART:
                if item["flower_name"] == self.flower_name:
                    if item["quantity"] > self.in_stock:
                        return True
        elif self.valid_order_quantity > self.in_stock:
            return True

    def bq_size_exceeded(self) -> Union[bool, None]:
        """
        Checks if items added to cart exceeds bouquet size
        :return: True if exceeds else None
        """
        if self.valid_order_quantity > BQ_SIZE[0]:
            return True

    def adding_to_cart(self) -> list:
        """
        Adds item to your cart and reduces the bouquet size
        :return: list of items in your cart
        """
        if len(YOUR_CART) > 0:
            new = 1
            # if new flower added already exists in your cart then only the quantity is added to previous order
            for item in YOUR_CART:
                if item["flower_name"] == self.flower_name:
                    item["quantity"] += self.valid_order_quantity
                    new = 0
            # if it's a new flower than new element is appended
            if new == 1:
                YOUR_CART.append(
                    {
                        "flower_name": self.flower_name,
                        "quantity": self.valid_order_quantity,
                        "price": self.price,
                    }
                )
        else:
            YOUR_CART.append(
                {
                    "flower_name": self.flower_name,
                    "quantity": self.valid_order_quantity,
                    "price": self.price,
                }
            )
        BQ_SIZE[0] -= self.valid_order_quantity
        return YOUR_CART

    @staticmethod
    def check_order_criteria() -> Union[bool, None]:
        """
        checks if bouquet size == 0
        :return: True if it is 0
        """
        if BQ_SIZE[0] == 0:
            return True

    @staticmethod
    def proceed_to_buy() -> str:
        """
        Updates the stock and clears items from your cart
        :return: success message
        """
        for item_1 in YOUR_CART:
            for item_2 in STOCK:
                if item_1["flower_name"] == item_2["flower_name"]:
                    item_2["quantity"] -= item_1["quantity"]
        YOUR_CART.clear()
        return "Order placed successfully"
