from flask import Flask

from . import site

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(site.site)
