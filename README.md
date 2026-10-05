# Sistema online para el control de inventario para un gimnasio

Este proyecto consiste en la creación de una **API con MongoDB** para un **gimnasio**, junto con un **frontend**. Este proyecto va a permitir a los dueños, o a los encargados del inventario, realizar las consultas necesarias para visualizar los activos que poseen. Además seran capaces de añadir, eliminar o modificar los diferentes equipos que posea el gimnasio.

##  Colecciones y Ejemplos

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