from flask import Blueprint, render_template
from flask import current_app as app
from flask_httpauth import HTTPBasicAuth

showcase = Blueprint('showcase', __name__)
auth = HTTPBasicAuth()


@auth.get_password
def get_pw(username):
    if username in app.config['SHOWCASE_ADMINS']:
        return app.config['SHOWCASE_ADMINS'][username]
    return None


@showcase.route('/')
def home():
    return 'Vitrine'


@showcase.route('/admin')
@auth.login_required
def admin_home():
    return 'Admin'
