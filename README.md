# Sistema online para el control de inventario para un gimnasio

Este proyecto consiste en la creación de una **API con MongoDB** para un **gimnasio**, junto con un **frontend**. Este proyecto va a permitir a los dueños, o a los encargados del inventario, realizar las consultas necesarias para visualizar los activos que poseen. Además seran capaces de añadir, eliminar o modificar los diferentes equipos que posea el gimnasio por medio de una interfaz gráfica

##  🎯 Colecciones y Ejemplos

### 👥 Entrenadores
```json
{
    "nombre":"Cristian",
    "apellido":"Cambronero",
    "numero":"8852-9512",
    "dia":"2026-10-01"
}
```

### 📘 Entrenadores suplentes
```json
{
    "nombre": "Elizabeth",
    "apellido2": "Campos",
    "numero": "7412-3698",
    "dia": "2026-09-18",
    "e_cubierto":{"nombre":"Roy"}
}
```

### 📅 Asistencia
```json
{
    "nombre":"Jose",
    "apellido":"Fonseca",
    "dia_asistido":"2026-09-30"
}
```
### 🏋️ Barras
```json
{
    "tipo":"Barra Z",
    "peso":"10 kg"
}
```
### 🏋️ Discos
```json
{
    "peso": "2.5 lbs",
    "cantidad":"6"
}
```
### 🏋️ Mancuernas
```json
{
    "peso":"5 lbs",
    "cantidad":"2"
}
```
### 🏋️ Máquinas
```json
{
    "nombre":"Rack",
    "cantidad":"1"
}
```

---


## 👤 Integrante del Proyecto

- Jose Pablo Fonseca Fernández

# 🔗 Endpoints de la base de datos Inventario GYM

### 1.Enpoints Asistencia

### Obtener todas las asistencias

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia`
* **Descripción:** Obtiene una lista de todas las asistencias del gimnasio

```http
GET http://127.0.0.1:5000/api/v1/Asistencia/asistencia
```

**Respuesta del endpoint:**

```json
[
    {
        "_id": "6ac120ba1a52d5320d6c6af4", 
        "nombre": "Jose", 
        "apellido": "Fonseca", 
        "dia_asistido": "2026-09-30"
    }, 
    {
        "_id": "6ac120c81a52d5320d6c6af5", 
        "nombre": "Valeria", 
        "apellido": "Pereira", 
        "dia_asistido": "2026-09-03"
     },
     {
        "_id": "6ac120c81a52d5320d6c6af6", 
        "nombre": "Natalia", 
        "apellido": "Solano", 
        "dia_asistido": "2026-10-02"
    },
    {
        "_id": "6ac120c81a52d5320d6c6af7", 
        "nombre": "Maria", 
        "apellido": "Gomez", 
        "dia_asistido": "2026-09-16"
    },
    {
        "_id": "6ac121421a52d5320d6c6af8", 
        "nombre": "Mariana", 
        "apellido": "Jimenez", 
        "dia_asistido": "2026-09-30"
    },
    {
        "_id": "6ac121421a52d5320d6c6af9", 
        "nombre": "Paola", 
        "apellido": "Hernandez", 
        "dia_asistido": "2026-10-03"
    },
    {
        "_id": "6ac121421a52d5320d6c6afa",
        "nombre": "Margarita",
        "apellido": "Mendez",
        "dia_asistido": "2026-09-02"
    },
    {
        "_id": "6ac1217d1a52d5320d6c6afb",
        "nombre": "Hernan", 
        "apellido": "Jimenez", 
        "dia_asistido": "2026-09-03"
    },
    {
        "_id": "6ac1217d1a52d5320d6c6afc", 
        "nombre": "Pedro", 
        "apellido": "Fernández", 
        "dia_asistido": "2026-10-02"
    }, 
    {
        "_id": "6ac1217d1a52d5320d6c6afd", 
        "nombre": "Rodrigo", 
        "apellido": "Campos", 
        "dia_asistido": "2026-09-30"
    },
    {
        "_id": "6ac6d37883d6bc779e5a9874", 
        "nombre": "Maria", 
        "apellido": "Rodriguez", 
        "dia_asistido": "2026-09-30"
    }, 
    {
        "_id": "6ac6d37883d6bc779e5a9876", 
        "nombre": "Ana", 
        "apellido": "Mora", 
        "dia_asistido": "2026-09-16"
    }, 
    {"_id": "6ac6d37883d6bc779e5a9875", 
    "nombre": "Carlos", 
    "apellido": "Jimenez", 
    "dia_asistido": "2026-10-02"
    }, 
    {
        "_id": "6ac6d37883d6bc779e5a9878", 
        "nombre": "Sofia", 
        "apellido": "Perez", 
        "dia_asistido": "2026-09-30"
    }, 
    {
        "_id": "6ae618081679f6e645f28e4a", 
        "nombre": "Maria", 
        "apellido": "Fonseca", 
        "dia_asistido": "31-10-2026"
    }]
```

### Agregar una asistencia nueva

* **Método:** `POST`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia_agregar`
* **Descripción:** Se registra una nueva asistencia.

```http
POST http://127.0.0.1:5000/api/v1/Asistencia/asistencia_agregar
```

**Datos de entrada del endpoint:**

```json
{
    "nombre":"Juana",
    "apellido":"Herrera",
    "dia_asistido":"30-11-2026"
}
```
**Respuesta del endpoint**

```json
{"message": "Asistencia creada exitosamente", "id": "6aea917e996e80c1d0021b81"}
```

## Modificar una asistencia

* **Método:** `PUT`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia_actualizar/`
* **Descripción:** Se modifica una asistencia existente.

```http
PUT http://127.0.0.1:5000/api/v1/Asistencia/asistencia_actualizar/6aea917e996e80c1d0021b81
```

**Datos de entrada del endpoint**

```json
{
    "nombre":"Juana",
    "apellido":"Campos",
    "dia_asistido":"30-11-2026"
}
```

**Respuesta del endpoint**

```json
{"Asistencia actualizada exitosamente ": "6aea917e996e80c1d0021b81"}
```

## Eliminar una asistencia

* **Método:** `DELETE`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia_eliminar/`
* **Descripción:** Se elimina una asistencia ya registrada del inventario.

```http
DELETE http://127.0.0.1:5000/api/v1/Asistencia/asistencia_eliminar/6aea917e996e80c1d0021b81
```

**Respuesta del endpoint**

```json
{"mensaje": "Asistencia con id 6aea917e996e80c1d0021b81 se elimino exitosamente"}
```

## Buscar una asistencia

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia_buscar/`
* **Descripción:** Se busca una asistencia que exista dentro del inventario.

```http
GET http://127.0.0.1:5000/api/v1/Asistencia/asistencia_buscar/6aea917e996e80c1d0021b85
```

**Respuesta del endpoint**

```json
{
    "_id": "6ac6d37883d6bc779e5a9878", 
    "nombre": "Sofia", 
    "apellido": "Perez", 
    "dia_asistido": "2026-09-30"
}
```

## Buscar una asistencia en una fecha en especifico

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia_buscar_por_fecha/`
* **Descripción:** Se busca la cantidad de personas que asistieron en una fecha al gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Asistencia/asistencia_buscar_por_fecha/2026-09-30
```

**Respuesta del endpoint**

```json
[{
    "_id": "{'fecha': '2026-09-30'}", 
    "Personas_que_asistieron_ese_dia": 5
}]
```

## Buscar una asistencia en un rango de fechas en especifico

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia_rango_fechas/<fecha_inicio>/<fecha_fin>`
* **Descripción:** Se busca la cantidad de personas que asistieron en un rango de fechas al gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Asistencia/asistencia_rango_fechas/2026-09-01/2026-10-01
```

**Respuesta del endpoint**

```json
[{
    "_id": "{'fecha': '2026-09-02'}", 
    "Personas_que_asistieron_ese_dia": 1
    }, 
    {
    "_id": "{'fecha': '2026-09-03'}", 
    "Personas_que_asistieron_ese_dia": 2
    }, 
    {
    "_id": "{'fecha': '2026-09-16'}", 
    "Personas_que_asistieron_ese_dia": 2
    },
    {
    "_id": "{'fecha': '2026-09-30'}", 
    "Personas_que_asistieron_ese_dia": 5
}]
```

### 2.Endpoints de Barras

### Obtener todas las Barras

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Barras/barras`
* **Descripción:** Obtiene una lista de todas las barras del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Barras/barras
```

**Respuesta del endpoint**

```json
[
    {
        "_id": "6ac036ef5655be6ce588d862", 
        "tipo": "Barra Z", 
        "peso": "10 kg"
    },
    {
        "_id": "6ac0379f5655be6ce588d864", 
        "tipo": "Olimpica", 
        "peso": "22 Kg"
    },
    {
        "_id": "6ac0379f5655be6ce588d865", 
        "tipo": "Olimpica negra", 
        "peso": "21 kg"
    },
    {
        "_id": "6ac0379f5655be6ce588d867", 
        "tipo": "Semi olimpica", 
        "peso": "12 kg"
    }
    ]
```

### Agregar una barra

* **Método:** `POST`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Barras/barras_agregar`
* **Descripción:** Se agrega una barra nueva al gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Barras/barras_agregar
```

**Datos de entrada del endpoint**

```json
{
    "tipo": "Barra de prueba",
    "peso": "25 Kg"
}
```

**Respuesta del endpoint**

```json
{"message": "Se agregó la barra exitosamente", "id": "6aeb5e3e4bb5a1940089904a"}
```

### Actualizar barras

* **Método:** `PUT`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Barras/barras_actualizar/`
* **Descripción:** Se actualiza una barra existente en el gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Barras/barras_actualizar/6aeb5e3e4bb5a1940089904a
```

**Datos de entrada del endpoint**

```json
{
    "tipo": "Barra de prueba",
    "peso": "30 Kg"
}
```

**Respuesta del endpoint**

```json
{"mensaje": "Se actualizó la barra con id 6aeb5e3e4bb5a1940089904a exitosamente"}
```

### Eliminar una barra

* **Método:** `DELETE`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Barras/barras_eliminar/`
* **Descripción:** Se elimina una barra del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Barras/barras_eliminar/6aeb5e3e4bb5a1940089904a
```

**Respuesta del endpoint**

```json
{"mensaje": "Se eliminó la barra con id 6aeb5e3e4bb5a1940089904a exitosamente"}
```

### Buscar una barra del gimnasio

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Barras/barras_buscar/`
* **Descripción:** Se busca una barra en el gimansio.

```http
GET http://127.0.0.1:5000/api/v1/Barras/barras_buscar/6ac0379f5655be6ce588d865
```


**Respuesta del endpoint**

```json
{"_id": "6ac0379f5655be6ce588d865", "tipo": "Olimpica negra", "peso": "21 kg"}
```

### 3.Endpoints de los discos

### Obtener todos los discos

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Discos/discos`
* **Descripción:** Obtiene una lista de todos los discos del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Discos/discos
```

**Respuesta del endpoint**

```json
[
    {
        "_id": "6ac03a175655be6ce588d869", 
        "peso": "5 lbs", 
        "cantidad": "8"
    },
    {
        "_id": "6ac03a175655be6ce588d86a", 
        "peso": "10 lbs", 
        "cantidad": "12"
    },
    {
        "_id": "6ac03a175655be6ce588d86b", 
        "peso": "25 lbs", 
        "cantida": "15"
    },
    {
        "_id": "6ac03a175655be6ce588d86c", 
        "peso": "35 lbs", 
        "cantidad": "8"
    },
    {
        "_id": "6ac03a175655be6ce588d86d", 
        "peso": "45 lbs", 
        "cantidad": "10"
    }
]
```

### Agregar un disco

* **Método:** `POST`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Discos/discos_agregar`
* **Descripción:** Se agrega un disco nuevo al gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Discos/discos_agregar
```

**Datos de entrada del endpoint**

```json
{ 
    "peso": "60 lbs", 
    "cantidad": "8"
}
```

**Respuesta del endpoint**

```json
{"message": "Se agregó el disco exitosamente", "id": "6aeb608b4bb5a1940089904b"}
```

### Actualizar un disco

* **Método:** `PUT`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Discos/discos_actualizar/`
* **Descripción:** Se actualiza un disco existente en el gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Discos/discos_actualizar/6aeb608b4bb5a1940089904b
```

**Datos de entrada del endpoint**

```json
{ 
    "peso": "60 lbs", 
    "cantidad": "6"
}
```

**Respuesta del endpoint**

```json
{"mensaje": "Se actualizó el disco con id 6aeb608b4bb5a1940089904b exitosamente"}
```

### Eliminar un disco

* **Método:** `DELETE`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Discos/discos_eliminar/`
* **Descripción:** Se elimina un disco del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Discos/discos_eliminar/6aeb608b4bb5a1940089904b
```

**Respuesta del endpoint**

```json
{"mensaje": "Se eliminó el disco con id 6aeb608b4bb5a1940089904b exitosamente"}
```

### Buscar un disco del gimnasio

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Discos/discos_buscar/`
* **Descripción:** Se busca un disco en el gimansio.

```http
GET http://127.0.0.1:5000/api/v1/Discos/discos_buscar/6ac03a175655be6ce588d86d
```


**Respuesta del endpoint**

```json
{"_id": "6ac03a175655be6ce588d86d", "peso": "45 lbs", "cantidad": "10"}
```

### 4.Endpoints de las mancuernas

### Obtener todas las mancuernas

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas`
* **Descripción:** Obtiene una lista de todas las mancuernas del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas
```

**Respuesta del endpoint**

```json
[
    {
        "_id": "6ac03c1b5655be6ce588d86f", 
        "peso": "8 lbs", 
        "cantidad": "4"
    },
    {
        "_id": "6ac03c1b5655be6ce588d870", 
        "peso": "10 lbs", 
        "cantidad": "8"
    },
    {
        "_id": "6ac03c1b5655be6ce588d871", 
        "peso": "15 lbs", 
        "cantidad": "10"
    },
    {
        "_id": "6ac03c1b5655be6ce588d872", 
        "peso": "20 lbs", 
        "cantidad": "8"
    },
    {
        "_id": "6ac03c1b5655be6ce588d873", 
        "peso": "25 lbs", 
        "cantidad": "6"
    }, 
    {
        "_id": "6ac03c1b5655be6ce588d874", 
        "peso": "30 lbs", 
        "cantidad": "8"
    },
    {
        "_id": "6ac03c1b5655be6ce588d875", 
        "peso": "35 lbs", 
        "cantidad": "4"
    },
    {
        "_id": "6ac03c1b5655be6ce588d876", 
        "peso": "40 lbs", 
        "cantidad": "4"
    },
    {
        "_id": "6ac03c1b5655be6ce588d877", 
        "peso": "45 lbs", 
        "cantidad": "4"
    },
    {
        "_id": "6ac03c1b5655be6ce588d878", 
        "peso": "50 lbs", 
        "cantidad": "2"
    },
    {
        "_id": "6ac03c1b5655be6ce588d879", 
        "peso": "66 lbs", 
        "cantidad": "2"
    }
]
```

### Agregar una mancuerna

* **Método:** `POST`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_agregar`
* **Descripción:** Se agrega una mancuerna nueva al gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_agregar
```

**Datos de entrada del endpoint**

```json
{ 
    "peso": "70 lbs", 
    "cantidad": "8"
}
```

**Respuesta del endpoint**

```json
{"message": "Se agregó la mancuerna exitosamente", "id": "6aeb63364bb5a1940089904c"}
```

### Actualizar una mancuerna

* **Método:** `PUT`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_actualizar/`
* **Descripción:** Se actualiza una mancuerna existente en el gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_actualizar/6aeb63364bb5a1940089904c
```

**Datos de entrada del endpoint**

```json
{ 
    "peso": "70 lbs", 
    "cantidad": "2"
}
```

**Respuesta del endpoint**

```json
{"mensaje": "Se actualizó la mancuerna con id 6aeb63364bb5a1940089904c exitosamente"}
```

### Eliminar una mancuerna

* **Método:** `DELETE`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_eliminar/`
* **Descripción:** Se elimina una mancuerna del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_eliminar/6aeb63364bb5a1940089904c
```

**Respuesta del endpoint**

```json
{"mensaje": "Se eliminó la mancuerna con id 6aeb63364bb5a1940089904c exitosamente"}
```

### Buscar una mancuerna 

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_buscar/`
* **Descripción:** Se busca una mancuerna en el gimansio.

```http
GET http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_buscar/6ac03c1b5655be6ce588d879
```


**Respuesta del endpoint**

```json
{"_id": "6ac03c1b5655be6ce588d879", "peso": "66 lbs", "cantidad": "2"}
```

### Top 5 mancuernas

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_top5`
* **Descripción:** Se obtienen las 5 mancuernas con más cantidad y sus pesos.

```http
http://127.0.0.1:5000/api/v1/Mancuernas/mancuernas_top5
```


**Respuesta del endpoint**

```json
[{
    "_id": "6ac03c1b5655be6ce588d874", 
    "peso": "30 lbs", 
    "cantidad": "8"
    }, 
    {
    "_id": "6ac03c1b5655be6ce588d870", 
    "peso": "10 lbs", 
    "cantidad": "8"
    },
    {
    "_id": "6ac03c1b5655be6ce588d872", 
    "peso": "20 lbs", 
    "cantidad": "8"
    },
    {
    "_id": "6ac03c1b5655be6ce588d873", 
    "peso": 
    "25 lbs", 
    "cantidad": "6"
    }, 
    {
    "_id": "6ac03c1b5655be6ce588d877", 
    "peso": "45 lbs", 
    "cantidad": "4"
    }
    ]
```

### 5.Endpoints de las máquinas

### Obtener todas las máquinas

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Maquinas/maquinas`
* **Descripción:** Obtiene una lista de todas las máquinas del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Maquinas/maquinas
```

**Respuesta del endpoint**

```json
[
    {
        "_id": "6ac03cd95655be6ce588d87a", 
        "nombre": "Rack", 
        "cantidad": "1"
    },
    {
        "_id": "6ac03efb5655be6ce588d889", 
        "nombre": "Extensión de rodilla", 
        "cantidad": "2"
    },
    {
        "_id": "6ac03efb5655be6ce588d88a", 
        "nombre": "Peck Deck", 
        "cantidad": "1"
    },
    {
        "_id": "6ac03efb5655be6ce588d88b", 
        "nombre": "Press de pierna", 
        "cantidad": "1"
    },
    {
        "_id": "6ac03efb5655be6ce588d88c", 
        "nombre": "Banca de flexión-rack", 
        "cantidad": "1"
    },
    {
        "_id": "6ac03efb5655be6ce588d88d", 
        "nombre": "Banca Plana", 
        "cantidad": "1"
    }, 
    {
        "_id": "6ac03efb5655be6ce588d88e", 
        "nombre": "Banca inclinada", 
        "cantidad": "2"
    },
    {
        "_id": "6ac03efb5655be6ce588d88f", 
        "nombre": "Press militar", 
        "cantidad": "1"
    },
    {
        "_id": "6ac03efb5655be6ce588d890", 
        "nombre": "Hip thrust", 
        "cantidad": "1"
    }, 
    {
        "_id": "6ac03efb5655be6ce588d891", 
        "nombre": "Spinning", 
        "cantidad": "2"
    },
    {
        "_id": "6ac03efb5655be6ce588d892", 
        "nombre": "Bicicleta reclinada", 
        "cantidad": "1"
    }, 
    {
        "_id": "6ac03efb5655be6ce588d893", 
        "nombre": "Sentadilla Sysy", 
        "cantidad": "1"
    },
    {
        "_id": "6ac03efb5655be6ce588d894", 
        "nombre": "Banco predicador", 
        "cantidad": "1"
    }
]
```

### Agregar una máquina

* **Método:** `POST`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Maquinas/maquinas_agregar`
* **Descripción:** Se agrega una máquina nueva al gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Maquinas/maquinas_agregar
```

**Datos de entrada del endpoint**

```json
{ 
    "nombre": "Máquina Prueba", 
    "cantidad": "2"
}
```

**Respuesta del endpoint**

```json
{"message": "Se agregó la maquina exitosamente", "id": "6aeb65894bb5a1940089904d"}
```

### Actualizar una máquina

* **Método:** `PUT`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Maquinas/maquinas_actualizar/`
* **Descripción:** Se actualiza una máquina existente en el gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Maquinas/maquinas_actualizar/6aeb65894bb5a1940089904d
```

**Datos de entrada del endpoint**

```json
{ 
    "nombre": "Máquina prueba", 
    "cantidad": "1"
}
```

**Respuesta del endpoint**

```json
{"mensaje": "Se actualizó la maquina con id 6aeb65894bb5a1940089904d exitosamente"}
```

### Eliminar una máquina

* **Método:** `DELETE`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Maquinas/maquinas_eliminar/`
* **Descripción:** Se elimina una máquina del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Maquinas/maquinas_eliminar/6aeb65894bb5a1940089904d
```

**Respuesta del endpoint**

```json
{"mensaje": "Se eliminó la maquina con id 6aeb65894bb5a1940089904d exitosamente"}
```

### Buscar una máquina 

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Maquinas/maquinas_buscar/`
* **Descripción:** Se busca una máquina en el gimansio.

```http
GET http://127.0.0.1:5000/api/v1/Maquinas/maquinas_buscar/6ac03efb5655be6ce588d88e
```


**Respuesta del endpoint**

```json
{"_id": "6ac03efb5655be6ce588d88e", "nombre": "Banca inclinada", "cantidad": "2"}
```

### Cantidad de máquinas en el gimnasio

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Maquinas/maquinas_cantidad`
* **Descripción:** Se busca una máquina en el gimansio.

```http
http://127.0.0.1:5000/api/v1/Maquinas/maquinas_cantidad
```


**Respuesta del endpoint**

```json
{"La cantidad de maquinas es de: ": 13}
```