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

### 2.Endpoints de Barras

### Obtener todas las Barras

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia`
* **Descripción:** Obtiene una lista de todas las barras del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Asistencia/asistencia
```

**Datos de entrada del endpoint**

```json
```

**Respuesta del endpoint**

```json
```

### Agregar una barra

* **Método:** `POST`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia`
* **Descripción:** Se agrega una barra nueva al gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Asistencia/asistencia
```

**Datos de entrada del endpoint**

```json
```

**Respuesta del endpoint**

```json
```

### Actualizar barras

* **Método:** `PUT`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia`
* **Descripción:** Se actualiza una barra existente en el gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Asistencia/asistencia
```

**Datos de entrada del endpoint**

```json
```

**Respuesta del endpoint**

```json
```

### Eliminar una barra

* **Método:** `DELETE`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia`
* **Descripción:** Se elimina una barra del gimnasio.

```http
GET http://127.0.0.1:5000/api/v1/Asistencia/asistencia
```

**Datos de entrada del endpoint**

```json
```

**Respuesta del endpoint**

```json
```

### Buscar una barra del gimnasio

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/api/v1/Asistencia/asistencia`
* **Descripción:** Se busca una barra en el gimansio.

```http
GET http://127.0.0.1:5000/api/v1/Asistencia/asistencia
```

**Datos de entrada del endpoint**

```json
```

**Respuesta del endpoint**

```json
```