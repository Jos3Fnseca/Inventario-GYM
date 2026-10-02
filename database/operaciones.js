//CRUD para inventario GYM

//Conexion a la base de datos

use("Inventario_Gym")

//------------------------
//Coleccion Entrenadores
//------------------------


//Insertar uno

db.Entrenadores.insertOne({
    nombre:'Cristian',
    apellido:'Cambronero',
    numero:'8852-9512',
    dia:'2026-10-01'
})

//Insertar varios registros

db.Entrenadores.insertMany([
    {
        nombre:'Roy',
        apellido:'Brenes',
        numero:'8745-2033',
        dia:'2026-09-30'
    },
    {
        nombre:'Ana Gabriel',
        apellido:'Tencio',
        numero:'8520-1245',
        dia:'2026-09-25'
    },
    {
        nombre:'Roy',
        apellido:'Brenes',
        numero:'8745-2033',
        dia:'2026-06-28'
    }

     ])

//Actualizar

db.Entrenadores.updateOne(
  { nombre: "Cristian" },
  { $set: { numero: "8521-0396" } }
);

//Eliminar

db.Entrenadores.deleteOne({ nombre: "Ana Gabriel" });

//------------------------
//Coleccion Entrenadores_Suplentes
//------------------------

//Agregar uno

db.Entrenadores_Suplentes.insertOne({
  nombre: 'Elizabeth',
  apellido: 'Campos',
  numero: '7412-3698',
  dia: '2026-09-18',
  e_cubierto:'Roy'
})

//Agregar varios

db.Entrenadores_Suplentes.insertMany([
    {
        nombre: 'Elizabeth',
        apellido: 'Campos',
        numero: '7412-3698',
        dia: '2026-09-18',
        e_cubierto:'Roy'
    },
    {
        nombre:'Allan',
        apellido:'Fonseca',
        numero:'8569-1254',
        dia:'2026-09-17',
        e_cubierto:'Cristian'
    },
    {
        nombre:'Katherine',
        apellido:'Rodriguez',
        numero:'3698-7412',
        e_cubierto:'Cristian'
    }])
//Actualizar 

db.Entrenadores_Suplentes.updateOne(
  { nombre: 'Allan' },
  { $set: { e_cubierto: 'Roy' } }
);
//Eliminar

db.Entrenadores_Suplentes.deleteOne({ nombre: "Katherine" });
//------------------------
//Coleccion Clientes
//------------------------

//Agregar uno
db.Clientes.insertOne({
  nombre:'Jose',
  apellido:'Fonseca',
  numero:'8968-1735',
  correo:'josefon@hotmail.com',
  dia_asistido:'2026-09-30'
})
//Agregar varios

db.Clientes.insertMany([{
  nombre:'Valeria',
  apellido:'Pereira',
  numero:'4569-9874',
  correo:'valper@gmail.com',
  dia_asistido:'2026-09-03'
},{
  nombre:'Natalia',
  apellido:'Solano',
  numero:'8520-0147',
  correo:'solanat@gmail.com',
  dia_asistido:'2026-10-02'
},{
  nombre:'Maria',
  apellido:'Romero',
  numero:'4521-0026',
  correo:'mariromero@hotmail.com',
  dia_asistido:'2026-09-16'
}])
//Actualizar 

db.Entrenadores_Suplentes.updateOne(
  { nombre: 'Allan' },
  { $set: { e_cubierto: 'Roy' } }
);
//Eliminar

db.Entrenadores_Suplentes.deleteOne({ nombre: "Katherine" });

//------------------------
//Coleccion Barras
//------------------------

//Agregar uno
//Agregar varios
//Actualizar 
//Eliminar
//------------------------
//Coleccion Discos
//------------------------

//Agregar uno
//Agregar varios
//Actualizar 
//Eliminar
//------------------------
//Coleccion Mancuernas
//------------------------

//Agregar uno
//Agregar varios
//Actualizar 
//Eliminar
//------------------------
//Coleccion Máquinas
//------------------------

//Agregar uno
//Agregar varios
//Actualizar 
//Eliminar
//------------------------
//Coleccion Otros
//------------------------

//Agregar uno
//Agregar varios
//Actualizar 
//Eliminar