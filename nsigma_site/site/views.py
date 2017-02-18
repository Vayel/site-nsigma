from flask import Blueprint, render_template, abort

site = Blueprint('site', __name__)


@site.route('/')
def home():
    return 'Site Nsigma'
