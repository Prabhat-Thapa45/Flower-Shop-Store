""" Has view functions to make order and handle the requests got from api """

from flask import flash, render_template, request

from src.order import Order, cancel
from src.utility.constants import BQ_SIZE, STOCK, YOUR_CART
from src.utility.validate_input import validate_int


def order_routes(app):
    """
    Renders templates for ordering flowers
    :param app:
    """

    @app.route("/menu/bouquet_size", methods=["GET", "POST"])
    def bouquet_size():
        """
        Takes valid bouquet size (1 to 200) and stores for further use
        """
        if request.method == "POST":
            size = request.form["bouquet_size"]
            valid_size = validate_int(size)
            if not valid_size:
                flash("Invalid entry", "danger")
                return render_template("bouquet_size.html")
            BQ_SIZE[0] = valid_size
            return render_template("show_flower.html", items=STOCK)
        return render_template("bouquet_size.html")

    @app.route("/menu/bouquet_size/add", methods=["POST"])
    def add_to_cart():
        """
        Takes valid user input and checks if it's in stock and if it's not exceeding bouquet size
        """
        if request.method == "POST":
            order_quantity = request.form["number"]
            flower_name = request.form["flower_name"]
            in_stock = int(request.form["in_stock"])
            price = float(request.form["price"])

            valid_order_quantity = validate_int(order_quantity)
            order = Order(valid_order_quantity, in_stock, flower_name, price)
            if not valid_order_quantity:
                flash("Invalid entry", "danger")
                return render_template("show_flower.html", items=STOCK), 400
            if order.flower_out_of_stock():
                flash(
                    "We are out of stock. You may order something else or cancel order",
                    "danger",
                )
                return render_template("show_flower.html", items=STOCK)
            if order.bq_size_exceeded():
                flash(
                    f"you have exceeded your bouquet size. You have {BQ_SIZE[0]} "
                    f"flowers left to add",
                    "danger",
                )
                return render_template("show_flower.html", items=STOCK)
            # adds items to your cart and reduces bq_size by valid_order_quantity
            order.adding_to_cart()
            flash(
                f"Flower added to cart. You have {BQ_SIZE[0]} flowers left to add",
                "success",
            )
            return render_template("show_flower.html", items=STOCK)

    @app.route("/menu/bouquet_size/go_to_cart", methods=["POST"])
    def go_to_cart():
        """
        checks if the total flowers added to cart is equal to bouquet size or not
        """
        if request.method == "POST":
            if not Order.check_order_criteria():
                flash(f"You still have {BQ_SIZE[0]} flowers left to order", "danger")
                return render_template("show_flower.html", items=STOCK)
            return render_template("go_to_cart.html", items=YOUR_CART)

    @app.route("/canceled", methods=["POST"])
    def cancel_order():
        if request.method == "POST":
            cancel()
            flash("Order canceled successfully", "success")
            return render_template("canceled.html")

    @app.route("/menu/bouquet_size/go_to_cart/buy", methods=["POST"])
    def buy() -> None or str:
        """
        Updates the stock and clears items from your cart
        """

        if request.method == "POST":
            flash(Order.proceed_to_buy(), "success")
            return render_template("order_placed.html")
