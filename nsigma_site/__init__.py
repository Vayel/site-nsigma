import os

from flask import Flask

from . import site
from . import showcase

app = Flask(__name__)

try:
    app.config.from_pyfile('flask.cfg')
except FileNotFoundError:
    pass

try:
    app.config.from_envvar('NSIGMA_SITE_FLASK_CONFIG_FILE') 
except RuntimeError:
    pass

app.register_blueprint(site.site)
app.register_blueprint(showcase.showcase, url_prefix='/vitrine')
