from flask import Blueprint, request, render_template, Response, flask
from flask import session as login_session
from flask_login import login_required, login_user, logout_user

from the_boiler.models import User

from the_boiler.webapp import database as db, app

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
# login_manager.login_view = "login


@app.route('/login', methods=['POST'])
def login():

    # login_user(user)
    return flask.redirect(flask.url_for('index'))


@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for('index'))
