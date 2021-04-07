from flask import Flask, request, make_response, Response
from flask_restful import Resource, Api

from services.random_movie import get_random_movie

class GetRandomMovie(Resource):
  def get(self):
    body = request.json
    try:
      genres = body['genres']
      genres_arr = genres.split(', ')
      return get_random_movie(genres_arr)
    except:
      return get_random_movie([])
