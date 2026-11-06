from flask import Blueprint, request, jsonify
from app.models.m_mancuernas import  M_Mancuernas
from app.utils.token import validar_token

mancuernas_endpoints = Blueprint('mancuernas', __name__)

def verificar_token():
    return validar_token()

@mancuernas_endpoints.route('/mancuernas', methods=['GET'])
def obtener_mancuernas():

    idmancuernas = request.args.get('id')
    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido

    if idmancuernas:
        mancuerna = M_Mancuernas.obtener_por_id(idmancuernas)
        if mancuerna:
            return jsonify(mancuerna), 200
        else:
            return jsonify({"error": "No se encontraron mancuernas en el inventario"}), 404

    mancuernas = M_Mancuernas.obtener_todos()
    return jsonify(mancuernas), 200


@mancuernas_endpoints.route('/mancuernas_agregar', methods=['POST'])
def crear_Mancuernas():
    
    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos de mancuernas vacios"}), 400

    # Validar los campos requeridos
    if "peso" not in data or "cantidad" not in data:
        return jsonify({"error": "Faltan campos requeridos para las mancuernas"}), 400

    #se crea la mancuerna
    mancuerna_id = M_Mancuernas.crear(data)
    return jsonify({"message": "Se agregó la mancuerna exitosamente", "id": str(mancuerna_id)}), 201

@mancuernas_endpoints.route('/mancuernas_actualizar/<id>', methods=['PUT'])
def actualizar_Mancuernas(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Datos de mancuernas vacios"}), 400

    resultado = M_Mancuernas.actualizar(id, data)
    if resultado == -1:
        return jsonify({"error": "Error al actualizar los datos de la mancuerna"}), 500

    return jsonify({"mensaje": f"Se actualizó la mancuerna con id {id} exitosamente"}), 200


@mancuernas_endpoints.route('/mancuernas_eliminar/<id>', methods=['DELETE'])
def eliminar_Mancuernas(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    resultado = M_Mancuernas.eliminar(id)
    if resultado == -1:
        return jsonify({"error": "Error al eliminar la mancuerna"}), 404

    return jsonify({"mensaje": f"Se eliminó la mancuerna con id {id} exitosamente"}), 200


@mancuernas_endpoints.route('/mancuernas_buscar/<id>', methods=['GET'])
def obtener_MancuernasId(id): 

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
      
    mancuerna = M_Mancuernas.obtener_por_id(id)
    if mancuerna is None:
        return jsonify({"error": "No se encontro la mancuerna que está buscando"}), 404

    return jsonify(mancuerna), 200