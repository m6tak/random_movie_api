from flask import Flask, request, make_response, Response
from flask_restful import Resource, Api

from api.get_random_movie import GetRandomMovie
from api.get_categories import GetCategories

app = Flask(__name__)
api = Api(app)

class Index(Resource):
  def get(self):
    return 'random movie api'

api.add_resource(GetRandomMovie, '/movie')
api.add_resource(GetCategories, '/categories')

if __name__ == '__main__':
  app.run(debug = True)