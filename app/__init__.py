from flask import Flask
from flask_restful import Api
import yaml
from .strip_loader import load_strips


app = Flask(__name__)
api = Api(app)
config = yaml.load(file('config.yaml', mode='r'))
strips = load_strips(config['strips'])

from . import api_views
