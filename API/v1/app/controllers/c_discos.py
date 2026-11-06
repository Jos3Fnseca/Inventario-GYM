from flask import Blueprint, request, jsonify
from app.models.m_discos import  M_Discos
from app.utils.token import validar_token

discos_endpoints = Blueprint('discos', __name__)

def verificar_token():
    return validar_token()

@discos_endpoints.route('/discos', methods=['GET'])
def obtener_discos():
    iddisco = request.args.get('id')

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    if iddisco:
        disco = M_Discos.obtener_por_id(iddisco)
        if disco:
            return jsonify(disco), 200
        else:
            return jsonify({"error": "No se encontraron discos en el inventario"}), 404

    discos = M_Discos.obtener_todos()
    return jsonify(discos), 200


@discos_endpoints.route('/discos_agregar', methods=['POST'])
def crear_Discos():
    
    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos de discos vacios"}), 400

    # Validar los campos requeridos
    if "peso" not in data or "cantidad" not in data:
        return jsonify({"error": "Faltan campos requeridos para los discos"}), 400

    #se crea el disco
    disco_id = M_Discos.crear(data)
    return jsonify({"message": "Se agregó el disco exitosamente", "id": str(disco_id)}), 201

@discos_endpoints.route('/discos_actualizar/<id>', methods=['PUT'])
def actualizar_Discos(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Datos de discos vacios"}), 400

    resultado = M_Discos.actualizar(id, data)
    if resultado == -1:
        return jsonify({"error": "Error al actualizar los datos del disco"}), 500

    return jsonify({"mensaje": f"Se actualizó el disco con id {id} exitosamente"}), 200


@discos_endpoints.route('/discos_eliminar/<id>', methods=['DELETE'])
def eliminar_Discos(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    resultado = M_Discos.eliminar(id)
    if resultado == -1:
        return jsonify({"error": "Error al eliminar el disco"}), 404

    return jsonify({"mensaje": f"Se eliminó el disco con id {id} exitosamente"}), 200


@discos_endpoints.route('/discos_buscar/<id>', methods=['GET'])
def obtener_DiscosId(id): 

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
      
    disco = M_Discos.obtener_por_id(id)
    if disco is None:
        return jsonify({"error": "No se encontro el disco que está buscando"}), 404

    return jsonify(disco), 200
