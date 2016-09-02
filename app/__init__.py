from flask import Flask
from flask_restful import Api
import yaml
from .strip_loader import load_strips
from .scheduler import get_scheduler
from plugins.plugin_loader import load_plugins
from .logs import setup_loggers
import logging


config = yaml.load(file('config.yaml', mode='r'))
app = Flask(__name__)
setup_loggers(app.logger, logging.getLogger('werkzeug'))
api = Api(app)
strips = load_strips(config['strips'])
scheduler = get_scheduler()

from . import api_views

load_plugins(config['runners'], scheduler, api_views.set_pixel)
