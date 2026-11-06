from flask import Blueprint, request, jsonify
from app.models.m_asistencia import M_Asistencia
from app.utils.token import validar_token

asistencia_endpoints = Blueprint('asistencia_endpoints', __name__)

def verificar_token():
    return validar_token()

@asistencia_endpoints.route('/asistencia', methods=['GET'])
def obtener_Asistencias():
    idAsistencia = request.args.get('id')

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido

    if idAsistencia:
        asistencia = M_Asistencia.obtener_por_id(idAsistencia)
        if asistencia:
            return jsonify(asistencia), 200
        else:
            return jsonify({"error": "Asistencia no encontrada"}), 404

    asistencia = M_Asistencia.obtener_todos()
    return jsonify(asistencia), 200

@asistencia_endpoints.route('/asistencia_agregar', methods=['POST'])
def crear_Asistencia():

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    data = request.get_json()


    if not data:
        return jsonify({"error": "Datos de asistencia vacios"}), 400

    # Validar los campos requeridos
    if "nombre" not in data or "apellido" not in data or "dia_asistido" not in data:
        return jsonify({"error": "Faltan campos requeridos para la asistencia"}), 400

    #se crea la asistencia
    asistencia_id = M_Asistencia.crear(data)
    return jsonify({"message": "Asistencia creada exitosamente", "id": str(asistencia_id)}), 201

@asistencia_endpoints.route('/asistencia_actualizar/<id>', methods=['PUT'])
def actualizar_Asistencia(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Datos de asistencia vacios"}), 400

    resultado = M_Asistencia.actualizar(id, data)
    if resultado == -1:
        return jsonify({"error": "Error al actualizar la asistencia"}), 500

    return jsonify({"Asistencia actualizada exitosamente ": id}), 200

@asistencia_endpoints.route('/asistencia_eliminar/<id>', methods=['DELETE'])
def eliminar_Asistencia(id):

    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    resultado = M_Asistencia.eliminar(id)
    if resultado == -1:
        return jsonify({"error": "Error al eliminar la asistencia"}), 404

    return jsonify({"mensaje": f"Asistencia con id {id} se elimino exitosamente"}), 200


@asistencia_endpoints.route('/asistencia_buscar/<id>', methods=['GET'])
def obtener_AsistenciaId(id):
    
    error_token = verificar_token()
    if error_token:
        return error_token  # Retorna el error de token si es inválido
    
    asistencia = M_Asistencia.obtener_por_id(id)
    if asistencia is None:
        return jsonify({"error": "Asistencia no encontrada"}), 404
    return jsonify(asistencia), 200
