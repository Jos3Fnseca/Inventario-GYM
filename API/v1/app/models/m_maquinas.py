from bson.objectid import ObjectId
from app import mongo

class M_Maquinas:
    @staticmethod
    def obtener_todos():
        maquinas_cursor = mongo.db.Maquinas.find()
        maquinas = []
        for maquina in maquinas_cursor:
            maquina['_id'] = str(maquina['_id'])  
            maquinas.append(maquina)
        return maquinas

    @staticmethod
    def obtener_por_id(id):
        try:
            maquina = mongo.db.Maquinas.find_one({"_id": ObjectId(id)})
            if maquina:
                maquina['_id'] = str(maquina['_id'])  
                return maquina
        except:
            return None

    @staticmethod
    def crear(maquina):
        try:
            result = mongo.db.Maquinas.insert_one(maquina)
            return result.inserted_id
        except:
            return None

    @staticmethod
    def actualizar(id, data):
        try:
            result = mongo.db.Maquinas.update_one({"_id": ObjectId(id)}, {"$set": data})
            return result.modified_count
        except:
            return -1

    @staticmethod
    def eliminar(id):
        try:
            result = mongo.db.Maquinas.delete_one({"_id": ObjectId(id)})
            return result.deleted_count
        except:
            return -1

