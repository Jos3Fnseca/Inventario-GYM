from bson.objectid import ObjectId
from app import mongo

class M_Mancuernas:
    @staticmethod
    def obtener_todos():
        mancuernas_cursor = mongo.db.Mancuernas.find()
        mancuernas = []
        for mancuerna in mancuernas_cursor:
            mancuerna['_id'] = str(mancuerna['_id'])  
            mancuernas.append(mancuerna)
        return mancuernas

    @staticmethod
    def obtener_por_id(id):
        try:
            mancuerna = mongo.db.Mancuernas.find_one({"_id": ObjectId(id)})
            if mancuerna:
                mancuerna['_id'] = str(mancuerna['_id'])  
                return mancuerna
        except:
            return None

    @staticmethod
    def crear(mancuerna):
        try:
            result = mongo.db.Mancuernas.insert_one(mancuerna)
            return result.inserted_id
        except:
            return None

    @staticmethod
    def actualizar(id, data):
        try:
            result = mongo.db.Mancuernas.update_one({"_id": ObjectId(id)}, {"$set": data})
            return result.modified_count
        except:
            return -1

    @staticmethod
    def eliminar(id):
        try:
            result = mongo.db.Mancuernas.delete_one({"_id": ObjectId(id)})
            return result.deleted_count
        except:
            return -1

    @staticmethod
    def top5():
        try:
            mancuernas_cursor = mongo.db.Mancuernas.find().sort("cantidad", -1).limit(5)
            mancuernas = []
            for mancuerna in mancuernas_cursor:
                mancuerna['_id'] = str(mancuerna['_id'])  
                mancuernas.append(mancuerna)
            return mancuernas
        except:
            return []