from flask import Flask, render_template, flash
from flask_login import LoginManager, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import flask_restless
import os
from config import config
# from celery import Celery


from the_boiler.celery_task import make_celery

config_name = os.getenv('BOILER_CONFIG', 'default')


def auth_func(*args, **kw):
    if not current_user.is_authenticated:
        raise ProcessingException(
            description='Not authenticated! Log in at http://localhost:5000/login', code=401)

# 1) create the flask application.
app = Flask(__name__)


app.config.from_object(config[config_name])

# 2) Set up the database. We can now import this anywhere.
database = SQLAlchemy(app)

# 3) Init Celery(app)
celery = make_celery(app)


# 4) Start Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# 5) Load App Blueprints
from the_boiler.mod_item.controllers import mod_items as item_module
from the_boiler.mod_auth.controllers import mod_auth as auth_module

# 6) Register blueprint(s)
app.register_blueprint(item_module)
app.register_blueprint(auth_module)

# Load User into


@login_manager.user_loader
def load_user(userid):
    from the_boiler.models import User
    return User.query.get(userid)


@app.route('/')
def index():
    return render_template('start.html')


@app.route('/secret')
@login_required
def secret():
    flash('Sending')
    return render_template('start.html')


@app.route('/h')
def heart():
    return 'alive'


def setup_app(config_name, app, database):
    """
    # Creates a JSON:API compliant REST application.

    :param config_name str: String name of the config.
    :param app: The application.
    :param database: SQLAlchemy database.
    """

    # 0) Import models. SQLAlchemy requires this during app initialization.
    import models

    # 2) Set up CORS.
    CORS(app)

    # 3) Get JSON: API compliant endpoints, based on models.
    apimanager = flask_restless.APIManager(
        app,
        flask_sqlalchemy_db=database)

    apimanager.create_api(models.Item, methods=['GET', 'POST', 'DELETE'])
    return apimanager


if __name__ == '__main__':
    app.run()
