from flask import Flask

app = Flask(__name__)


def init_app(settings):
    app.config.from_object(settings)
    return app
