from flask import Flask, request, make_response, Response
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
      genres_arr = genres.split(', ')
      return get_random_movie(genres_arr, start_year, end_year)
    except:
      traceback.print_exc()
      return get_random_movie([])
