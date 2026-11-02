from bson.objectid import ObjectId
from app import mongo

class M_Discos:
    @staticmethod
    def obtener_todos():
        discos_cursor = mongo.db.Discos.find()
        discos = []
        for disco in discos_cursor:
            disco['_id'] = str(disco['_id'])  
            discos.append(disco)
        return discos

    @staticmethod
    def obtener_por_id(id):
        try:
            disco = mongo.db.Discos.find_one({"_id": ObjectId(id)})
            if disco:
                disco['_id'] = str(disco['_id'])  
                return disco
        except:
            return None

    @staticmethod
    def crear(disco):
        try:
            result = mongo.db.Discos.insert_one(disco)
            return result.inserted_id
        except:
            return None

    @staticmethod
    def actualizar(id, data):
        try:
            result = mongo.db.Discos.update_one({"_id": ObjectId(id)}, {"$set": data})
            return result.modified_count
        except:
            return -1

    @staticmethod
    def eliminar(id):
        try:
            result = mongo.db.Discos.delete_one({"_id": ObjectId(id)})
            return result.deleted_count
        except:
            return -1