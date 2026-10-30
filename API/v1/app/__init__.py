from flask import Flask, app
from pymongo import PyMongo
from flask_cors import CORS
import os
from dotenv import load_dotenv

mongo = PyMongo()

def create_app():
    load_dotenv() 
    app = Flask(__name__)

    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    mongo.init_app(app)
    CORS(app, origins="*")

    from app.controllers.c_asistencia import asistencia_endpoints
    app.register_blueprint(asistencia_endpoints, url_prefix='/asistencia/api/v1')

    return app
