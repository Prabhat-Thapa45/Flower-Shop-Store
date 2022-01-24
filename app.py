from flask import Flask
from src.welcome_api import welcome_routes
from src.order_api import order_routes
from src.add_flower_api import add_flower_routes

app = Flask(__name__)
welcome_routes(app)
order_routes(app)
add_flower_routes(app)

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
