from bson.objectid import ObjectId
from app import mongo


class M_Asistencia:
    @staticmethod
    def obtener_todos():
        print("Se entró al modelo")
        asistencia_cursor = mongo.db.Asistencia.find()
        asistencias = []
        for asistencia in asistencia_cursor:
            asistencia['_id'] = str(asistencia['_id'])  
            asistencias.append(asistencia)
        return asistencias

    @staticmethod
    def obtener_por_id(id):

        try:
            asistencia = mongo.db.Asistencia.find_one({"_id": ObjectId(id)})
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
            result = mongo.db.Asistencia.insert_one(asistencia)
            return result.inserted_id
        except:
            return None

    @staticmethod
    def actualizar(id, data):
        try:
            result = mongo.db.Asistencia.update_one({"_id": ObjectId(id)}, {"$set": data})
            return result.modified_count
        except:
            return -1

    @staticmethod
    def eliminar(id):
        try:
            result = mongo.db.Asistencia.delete_one({"_id": ObjectId(id)})
            return result.deleted_count
        except:
            return -1

    @staticmethod
    def buscar_por_fecha(dia_asistido):
        try:
            asistencia_cursor = mongo.db.Asistencia.aggregate([
                {"$match": {"dia_asistido": dia_asistido}},
                {"$group": {"_id": {"fecha": "$dia_asistido"}, "Personas_que_asistieron_ese_dia": {"$sum": 1}}}
            ])
            asistencias = []
            for asistencia in asistencia_cursor:
                asistencia['_id'] = str(asistencia['_id'])  
                asistencias.append(asistencia)
            return asistencias
        except:
            return []

    @staticmethod
    def buscar_rango_fechas(fecha_inicio, fecha_fin):
        try:
            asistencia_cursor = mongo.db.Asistencia.aggregate([
                {"$match": {"dia_asistido": {"$gte": fecha_inicio, "$lte": fecha_fin}}},
                {"$group": {"_id": {"fecha": "$dia_asistido"}, "Personas_que_asistieron_ese_dia": {"$sum": 1}}},
                {"$sort": {"_id.fecha": 1}}
            ])
            asistencias = []
            for asistencia in asistencia_cursor:
                asistencia['_id'] = str(asistencia['_id'])  
                asistencias.append(asistencia)
            return asistencias
        except:
            return []

                
               