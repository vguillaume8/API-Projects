from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [

    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class User(Resource):
    def get(self, name):

    def post(self, name):

    def put(self, name):

    def put(self, name):

    def delete(self, name):
