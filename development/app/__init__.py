from flask import Flask
from app.model import init_models
from .extensions import init_ext
from app.views import config_blueprint
from .config import config_map

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])
    config_map[config_name].init_app(app)
    config_blueprint(app)
    init_models(app)
    init_ext(app)
    return app
