from flask import Flask, request, make_response, Response, abort
from flask_restful import Resource, Api

from services.random_movie import get_random_movie
import traceback

class GetRandomMovie(Resource):
  def post(self):
    body = request.json
    try:
      print(body);
      genres = body['genres']
      start_year = body['startYear']
      end_year = body['endYear']
      return get_random_movie(genres, start_year, end_year)
    except:
      abort(404)
