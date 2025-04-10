from flask import Flask

def create_app():
    app = Flask(__name__)
    from . import routes
    return app