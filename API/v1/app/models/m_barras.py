from bson.objectid import ObjectId
from app import mongo

class M_Barras:
    @staticmethod
    def obtener_todos():
        barras_cursor = mongo.db.Barras.find()
        barras = []
        for barra in barras_cursor:
            barra['_id'] = str(barra['_id'])  
            barras.append(barra)
        return barras

    @staticmethod
    def obtener_por_id(id):
        try:
            barra = mongo.db.Barras.find_one({"_id": ObjectId(id)})
            if barra:
                barra['_id'] = str(barra['_id'])  
                return barra
        except:
            return None

    @staticmethod
    def crear(barra):
        try:
            result = mongo.db.Barras.insert_one(barra)
            return result.inserted_id
        except:
            return None

    @staticmethod
    def actualizar(id, data):
        try:
            result = mongo.db.Barras.update_one({"_id": ObjectId(id)}, {"$set": data})
            return result.modified_count
        except:
            return -1

    @staticmethod
    def eliminar(id):
        try:
            result = mongo.db.Barras.delete_one({"_id": ObjectId(id)})
            return result.deleted_count
        except:
            return -1