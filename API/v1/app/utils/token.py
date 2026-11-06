from flask import request, jsonify
from datetime import datetime
from app import mongo

def validar_token():
    auth = request.headers.get('Authorization')

    if not auth or not auth.startswith('Bearer '):
        return jsonify({"error": "No se ingreso el token."}), 401

    token = auth.split(" ")[1]

    documento_token = mongo.db.Token.find_one({"token": token})

    if not documento_token:
        return jsonify({"error": "Token de autorización no encontrado"}), 401

    print(token)
    return None  # Token válido, continuar con la solicitud