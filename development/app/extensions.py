from flask import url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate(db=db)
bootstrap = Bootstrap()
mail = Mail()
login_manage = LoginManager()
cache = Cache(config={
    "CACHE_TYPE":"simple"
})

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app)
    login_manage.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    # DebugToolbarExtension(app)

    login_manage.login_view = 'index_blue.login'
    login_manage.login_message = '你还没有登录'
    login_manage.session_protection = "strong"
    login_manage.login_message_category = "info"
