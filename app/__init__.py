"""
The init file of the main application
NOTE: __init__.py is a special Python file that allows a directory to become
a Python package so it can be accessed using the 'import' statement
"""
from flask import Flask
from flask_user import UserManager, SQLAlchemyAdapter
# CSRF
from flask_wtf.csrf import CSRFProtect
# Models
from app.models import DB, MIGRATE, User
# Routes
from app.promo.routes import MOD_PROMO, SOCKETIO
from app.users.routes import MOD_USER
# Models DB Adaptor
# Flask Migrations
from flask_migrate import Migrate
# Flask Mail
from flask_mail import Mail
# Registration Form
from app.users.forms import MyRegisterForm


# Flask Initialization
APP = Flask(__name__, static_folder=None)

# Configuration
APP.config.from_object('config.ProductionConfig')

# Database Initialization
DB.init_app(APP)

# Flask Mail initializaed
MAIL = Mail(APP)

# CSRF Protection
CSRF = CSRFProtect(APP)

# Flask User Initialization
# USER_MANAGER = UserManager(DB_ADAPTER, APP)

# Flask Migrations Initialization
MIGRATE.init_app(APP, DB)


# Blueprint Registration
APP.register_blueprint(MOD_PROMO)
APP.register_blueprint(MOD_USER)

DATABASEADAPTER = SQLAlchemyAdapter(DB, User)
USERMANAGER = UserManager(DATABASEADAPTER, APP, register_form=MyRegisterForm)

# SocketIO initialization
SOCKETIO.init_app(APP)

if __name__ == '__main__':
    APP.jinja_env.cache = {}
    SOCKETIO.run(APP)
