from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource
from src import signature_detection
from exceptions import *
import json


class SignatureDetector(Resource):
    def post(self):
        try:
            return signature_detection.guess_result(request.json)
        except BadEntryError as error:
            return {'message': str(error)}, 400
        
app = Flask(__name__)
CORS(app)

api = Api(app)

api.add_resource(SignatureDetector, "/is_signer")


if __name__ == "__main__":
    app.run(host='127.0.0.1')