from flask import Flask, app
from flask_pymongo import PyMongo
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
    app.register_blueprint(asistencia_endpoints, url_prefix='/api/v1/Asistencia')

    from app.controllers.c_barras import barras_endpoints
    app.register_blueprint(barras_endpoints, url_prefix='/api/v1/Barras')

    from app.controllers.c_discos import discos_endpoints
    app.register_blueprint(discos_endpoints, url_prefix='/api/v1/Discos')

    from app.controllers.c_mancuernas import mancuernas_endpoints
    app.register_blueprint(mancuernas_endpoints, url_prefix='/api/v1/Mancuernas')

    from app.controllers.c_maquinas import maquinas_endpoints
    app.register_blueprint(maquinas_endpoints, url_prefix='/api/v1/Maquinas')

    return app
