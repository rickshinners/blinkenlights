from . import api, strips
from flask_restful import Resource, reqparse


class Pixel(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('rgb', type=list, location='json')

    def get(self, strip_name, index):
        return strips[strip_name].get_config(index)

    def put(self, strip_name, index):
        args = self.parser.parse_args()
        (r, g, b) = tuple(args['rgb'])
        strips[strip_name].set(index, r, g, b)
        return self.get(strip_name, index)


class Pixels(Resource):
    def get(self, strip_name):
        return strips[strip_name].get_config_all()


api.add_resource(Pixel, '/<string:strip_name>/<int:index>')
api.add_resource(Pixels, '/<string:strip_name>', '/<string:strip_name>/')