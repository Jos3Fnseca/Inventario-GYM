from bson.objectid import ObjectId
from app import mongo


class M_Asistencia:
    @staticmethod
    def obtener_todos():
        print("Se entroó al modelo")
        asistencia_cursor = mongo.db.asistencia.find()
        asistencia_list = []
        for asistencia in asistencia_cursor:
            asistencia['_id'] = str(asistencia['_id'])  
            asistencia_list.append(asistencia)
            return asistencia_list

    @staticmethod
    def obtener_por_id(id):

        try:
            asistencia = mongo.db.asistencia.find_one({"_id": ObjectId(id)})
            if asistencia:
                asistencia['_id'] = str(asistencia['_id'])  
                return asistencia
        except:
            return None

    @staticmethod
    def crear(asistencia):
        print("En el modelo")
        print(asistencia)
        try:
            result = mongo.db.asistencia.insert_one(asistencia)
            return result.inserted_id
        except Exception as e:
            return None

    @staticmethod
    def actualizar(id, data):
        try:
            result = mongo.db.asistencia.update_one({"_id": ObjectId(id)}, {"$set": data})
            return result.modified_count
        except:
            return -1

    @staticmethod
    def eliminar(id):
        try:
            result = mongo.db.asistencia.delete_one({"_id": ObjectId(id)})
            return result.deleted_count
        except:
            return -1
                
               