""" has all the view functions for initial welcome pages """

from flask import render_template


def welcome_routes(app):
    """
    Renders templates for initial pages
    :param app:
    """

    @app.route("/")
    @app.route("/home")
    def index() -> str:
        return render_template("index.html")

    @app.route("/about")
    def about() -> str:
        return render_template("about.html")

    @app.route("/contact")
    def contact() -> str:
        return render_template("contact.html")

    @app.route("/menu")
    def menu():
        return render_template("menu.html")
