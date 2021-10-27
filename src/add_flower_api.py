""" has all the view functions to route for adding new or in stock of existing flower """

from typing import Union

from flask import Response, flash, redirect, render_template, request, url_for

from src.add_flower import AddFlower
from src.utility.constants import STOCK
from src.utility.validate_input import validate_float, validate_int


def add_flower_routes(app):
    """
    Renders templates for adding flowers in stock
    :param app:
    """

    @app.route("/menu/add_flower", methods=["GET", "POST"])
    def add_flower() -> Union[str, Response]:
        """
        Takes valid amount to add and adds to stock
        """
        if request.method == "POST":
            flowers_to_add = request.form["number"]
            flower_name = request.form["flower_name"]

            valid_amount_to_add = validate_int(flowers_to_add)
            if not valid_amount_to_add:
                flash("Invalid entry", "danger")
                return redirect(url_for("add_flower", items=STOCK))
            add = AddFlower(flower_name)
            add.add_to_stock(valid_amount_to_add)
            return redirect(url_for("add_flower", items=STOCK))
        return render_template("add_flower.html", items=STOCK)

    @app.route("/menu/add_flower/add_new_flower", methods=["GET", "POST"])
    def add_new_flower() -> Union[str, Response]:
        """
        Adds new flower if flower already exists adds quantity while updates the price
        """
        if request.method == "POST":
            flower_name = request.form["flower_name"]
            quantity = request.form["quantity"]
            price = request.form["price"]
            valid_quantity = validate_int(quantity)
            valid_price = validate_float(price)
            if not valid_quantity or not valid_price:
                flash("Invalid entry", "danger")
                return render_template("add_new_flower.html")
            add = AddFlower(flower_name)
            add.add_new_in_stock(valid_quantity, valid_price)
            return redirect(url_for("add_flower", items=STOCK))
        return render_template("add_new_flower.html")
