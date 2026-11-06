from flask import Blueprint, request, jsonify
from app.models.m_barras import M_Barras
from app.utils.token import validar_token

barras_endpoints = Blueprint('barras_endpoints', __name__)

def verificar_token():
    return validar_token()

@barras_endpoints.route('/barras', methods=['GET'])
def obtener_Barras():
    idBarras = request.args.get('id')

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido

    if idBarras:
        barra = M_Barras.obtener_por_id(idBarras)
        if barra:
            return jsonify(barra), 200
        else:
            return jsonify({"error": "No se encontraron barras"}), 404

    barras = M_Barras.obtener_todos()
    return jsonify(barras), 200


@barras_endpoints.route('/barras_agregar', methods=['POST'])
def crear_Barras():

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos de barras vacios"}), 400

    # Validar los campos requeridos
    if "tipo" not in data or "peso" not in data:
        return jsonify({"error": "Faltan campos requeridos para las barras"}), 400

    #se crea la barra
    barra_id = M_Barras.crear(data)
    return jsonify({"message": "Se agregó la barra exitosamente", "id": str(barra_id)}), 201


@barras_endpoints.route('/barras_actualizar/<id>', methods=['PUT'])
def actualizar_Barras(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Datos de barras vacios"}), 400

    resultado = M_Barras.actualizar(id, data)
    if resultado == -1:
        return jsonify({"error": "Error al actualizar los datos de la barra"}), 500

    return jsonify({"mensaje": f"Se actualizó la barra con id {id} exitosamente"}), 200


@barras_endpoints.route('/barras_eliminar/<id>', methods=['DELETE'])
def eliminar_Barras(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    resultado = M_Barras.eliminar(id)
    if resultado == -1:
        return jsonify({"error": "Error al eliminar la barra"}), 404

    return jsonify({"mensaje": f"Se eliminó la barra con id {id} exitosamente"}), 200


@barras_endpoints.route('/barras_buscar/<id>', methods=['GET'])
def obtener_BarrasId(id):  
     
    error_token = verificar_token()
    if error_token: 
        return error_token  # Retorna el error de token si es inválido
    
    barra = M_Barras.obtener_por_id(id)
    if barra is None:
        return jsonify({"error": "No se encontro la barra que está buscando"}), 404

    return jsonify(barra), 200


