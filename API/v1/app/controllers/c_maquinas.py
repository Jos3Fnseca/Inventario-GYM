from flask import Blueprint, request, jsonify
from app.models.m_maquinas import  M_Maquinas
from app.utils.token import validar_token

maquinas_endpoints = Blueprint('maquinas', __name__)

def verificar_token():
    return validar_token()

@maquinas_endpoints.route('/maquinas', methods=['GET'])
def obtener_maquinas():
    idmaquinas = request.args.get('id')

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido


    if idmaquinas:
        maquina = M_Maquinas.obtener_por_id(idmaquinas)
        if maquina:
            return jsonify(maquina), 200
        else:
            return jsonify({"error": "No se encontraron maquinas en el inventario"}), 404

    maquinas = M_Maquinas.obtener_todos()
    return jsonify(maquinas), 200


@maquinas_endpoints.route('/maquinas_agregar', methods=['POST'])
def crear_Maquinas():

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos de maquinas vacios"}), 400

    # Validar los campos requeridos
    if "nombre" not in data or "cantidad" not in data:
        return jsonify({"error": "Faltan campos requeridos para las maquinas"}), 400

    #se crea la maquina
    maquina_id = M_Maquinas.crear(data)
    return jsonify({"message": "Se agregó la maquina exitosamente", "id": str(maquina_id)}), 201

@maquinas_endpoints.route('/maquinas_actualizar/<id>', methods=['PUT'])
def actualizar_Maquinas(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Datos de maquinas vacios"}), 400

    resultado = M_Maquinas.actualizar(id, data)
    if resultado == -1:
        return jsonify({"error": "Error al actualizar los datos de la maquina"}), 500

    return jsonify({"mensaje": f"Se actualizó la maquina con id {id} exitosamente"}), 200


@maquinas_endpoints.route('/maquinas_eliminar/<id>', methods=['DELETE'])
def eliminar_Maquinas(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    resultado = M_Maquinas.eliminar(id)
    if resultado == -1:
        return jsonify({"error": "Error al eliminar la maquina"}), 404

    return jsonify({"mensaje": f"Se eliminó la maquina con id {id} exitosamente"}), 200


@maquinas_endpoints.route('/maquinas_buscar/<id>', methods=['GET'])
def obtener_MaquinasId(id):  

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
     
    maquina = M_Maquinas.obtener_por_id(id)
    if maquina is None:
        return jsonify({"error": "No se encontro la maquina que está buscando"}), 404

    return jsonify(maquina), 200

@maquinas_endpoints.route('/maquinas_cantidad', methods=['GET'])
def obtener_cantidad_maquinas():

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido

    cantidad = M_Maquinas.cantidad_maquinas()
    if cantidad == -1:
        return jsonify({"error": "Hubo un error, intentelo de nuevo más tarde"}), 500

    return jsonify({"La cantidad de maquinas es de: ": cantidad}), 200