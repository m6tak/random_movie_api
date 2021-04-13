from flask import Flask, request, make_response, Response
from flask_restful import Resource, Api

from services.categories import categories

class GetCategories(Resource):
  def get(self):
    return categories