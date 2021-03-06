from flask import Flask

from App.web import init_webBlue
from App.ext import init_ext
from App.settings import envs
from App.nationApi import init_nationBlue


def create_app():
    app = Flask(__name__)
    app.config.from_object(envs.get('dev'))
    init_webBlue(app)
    init_ext(app)
    init_nationBlue(app)
    return app

