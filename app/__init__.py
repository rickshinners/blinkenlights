from flask import Flask
from .scheduler import get_scheduler
from .logs import setup_loggers
import logging


app = Flask(__name__, static_url_path='', static_folder='static')
setup_loggers(app.logger, logging.getLogger('werkzeug'), logging.getLogger('apscheduler'))
scheduler = get_scheduler()
strips = {}

def set_pixel(strip_name, index, r, g, b):
    strips[strip_name].set(index, r, g, b)

from .strip_loader import load_configuration_file
from . import api_views

load_configuration_file('config.yaml')
