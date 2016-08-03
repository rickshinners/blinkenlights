from flask import Flask
from flask_restful import Api
import yaml
from .strip_loader import load_strips
from .scheduler import get_scheduler
from plugins.plugin_loader import load_plugins


app = Flask(__name__)
api = Api(app)
config = yaml.load(file('config.yaml', mode='r'))
strips = load_strips(config['strips'])
scheduler = get_scheduler()

from . import api_views

load_plugins(config['runners'], scheduler)
