from . import strips, app, set_pixel
from flask_restful import Resource, reqparse, Api
from strip_loader import load_configuration_file


class Pixel(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('rgb', type=list, location='json')

    def get(self, strip_name, index):
        return strips[strip_name].get_config(index)

    def put(self, strip_name, index):
        args = self.parser.parse_args()
        (r, g, b) = tuple(args['rgb'])
        set_pixel(strip_name, index, r, g, b)
        return self.get(strip_name, index)


class Pixels(Resource):
    def get(self, strip_name):
        return strips[strip_name].get_config_all()


class Reload(Resource):
    def get(self):
        load_configuration_file('config.yaml')
        return "Success", 200

api = Api(app)

api.add_resource(Pixel, '/strips/<string:strip_name>/<int:index>')
api.add_resource(Pixels, '/strips/<string:strip_name>', '/strips/<string:strip_name>/')
api.add_resource(Reload, '/reload')