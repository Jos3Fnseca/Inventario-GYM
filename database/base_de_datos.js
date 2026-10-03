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
  { nombre: 'Cristian' },
  { $set: { numero: '8521-0396' } }
);

//Eliminar

db.Entrenadores.deleteOne({ nombre: 'Ana Gabriel' });

//------------------------
//Coleccion Entrenadores_Suplentes
//------------------------

//Agregar uno

db.Entrenadores_Suplentes.insertOne({
  nombre: 'Elizabeth',
  apellido: 'Campos',
  numero: '7412-3698',
  dia: '2026-09-18',
  e_cubierto:{nombre:'Roy'}
})

//Agregar varios

db.Entrenadores_Suplentes.insertMany([
    {
        nombre: 'Elizabeth',
        apellido: 'Campos',
        numero: '7412-3698',
        dia: '2026-09-17',
        e_cubierto:{nombre:'Roy'}
    },
    {
        nombre:'Allan',
        apellido:'Fonseca',
        numero:'8569-1254',
        dia:'2026-09-17',
        e_cubierto:{nombre:'Cristian'}
    },
    {
        nombre:'Katherine',
        apellido:'Rodriguez',
        numero:'3698-7412',
        dia:'2026-09-30',
        e_cubierto:{nombre:'Cristian'}
    },{
      nombre:'Allan',
      apellido:'Fonseca',
      numero:'8569-1254',
      dia:'2026-09-26',
      e_cubierto:{nombre:'Cristian'}
    }])

//Actualizar 

db.Entrenadores_Suplentes.updateOne(
  { nombre: 'Elizabeth', dia: '2026-09-17' },
  { $set: { dia: '2026-09-10' } }
)

//Eliminar

db.Entrenadores_Suplentes.deleteOne({ nombre: 'Katherine' });

//------------------------
//Coleccion Asistencia
//------------------------

//Agregar uno

db.Asistencia.insertOne({
  nombre:'Jose',
  apellido:'Fonseca',
  dia_asistido:'2026-09-30'
})

//Agregar varios

db.Asistencia.insertMany([{
  nombre:'Valeria',
  apellido:'Pereira',
  dia_asistido:'2026-09-03'
},{
  nombre:'Natalia',
  apellido:'Solano',
  dia_asistido:'2026-10-02'
},{
  nombre:'Maria',
  apellido:'Romero',
  dia_asistido:'2026-09-16'
}])

//Actualizar 

db.Asistencia.updateOne(
  { nombre: 'Maria' },
  { $set: { apellido: 'Gomez' } }
);

//Eliminar

db.Clientes.deleteOne({ nombre: 'Maria' });

//------------------------
//Coleccion Barras
//------------------------

//Agregar uno

db.Barras.insertOne({
  tipo:'Barra Z',
  peso:'10 kg'
})

//Agregar varios

db.Barras.insertMany([{
  tipo:'Olimpica',
  peso:'20 kg'
},{
  tipo:'Olimpica negra',
  peso:'21 kg'
},{
  tipo:'Barra en H',
  peso:'10 kg'
},{
  tipo:'Semi olimpica',
  peso:'12 kg'
}])

//Actualizar 

db.Barras.updateOne(
  { tipo: 'Barra H' },
  { $set: { peso: '8 kg' } }
);

//Eliminar

db.Barras.deleteOne({ tipo: 'Barra en H' });

//------------------------
//Coleccion Discos
//------------------------

//Agregar uno

db.Discos.insertOne({
  peso: '2.5 lbs',
  cantidad:'6'
})

//Agregar varios

db.Discos.insertMany([{
  peso:'5 lbs',
  cantidad:'8'
},{
  peso:'10 lbs',
  cantidad:'10'
},{
  peso:'25 lbs',
  cantida:'15'
},{
  peso:'35 lbs',
  cantidad:'8'
},{
  peso:'45 lbs',
  cantidad:'10'
}])

//Actualizar 

db.Discos.updateOne(
  { peso: '10 lbs' },
  { $set: { cantidad: '12' } }
);

//Eliminar

db.Discos.deleteOne({ peso: '2.5 lbs' });

//------------------------
//Coleccion Mancuernas
//------------------------

//Agregar uno

db.Mancuernas.insertOne({
  peso:'5 lbs',
  cantidad:'2'
})

//Agregar varios

db.Mancuernas.insertMany([{
  peso:'8 lbs',
  cantidad:'4',
},{
  peso:'10 lbs',
  cantidad:'6'
},{
  peso:'15 lbs',
  cantidad:'10'
},{
  peso:'20 lbs',
  cantidad:'8'
},{
  peso:'25 lbs',
  cantidad:'6'
},{
  peso:'30 lbs',
  cantidad:'8'
},{
  peso:'35 lbs',
  cantidad:'4'
},{
  peso:'40 lbs',
  cantidad:'4'
},{
  peso:'45 lbs',
  cantidad:'4'
},{
  peso:'50 lbs',
  cantidad:'2'
},{
  peso:'66 lbs',
  cantidad:'2'
}
])

//Actualizar 

db.Mancuernas.updateOne(
  { peso: '10 lbs' },
  { $set: { cantidad: '8' } }
);

//Eliminar

db.Mancuernas.deleteOne({ peso: '5 lbs' });

//------------------------
//Coleccion Máquinas
//------------------------

//Agregar uno

db.Maquinas.insertOne({
  nombre:'Rack',
  cantidad:'1'
})

//Agregar varios

db.Maquinas.insertMany([{
  nombre:'Cross over',
  cantidad:'1'
},{
  nombre:'Extensión de rodilla',
  cantidad:'2'
},{
  nombre:'Peck Deck',
  cantidad:'1'
},{
  nombre:'Press de pierna',
  cantidad:'1'
},{
  nombre:'Banca de flexión-rack',
  cantidad:'1'
},{
  nombre:'Banca Plana',
  cantidad:'1'
},{
  nombre:'Banca inclinada',
  cantidad:'2'
},{
  nombre:'Press militar',
  cantidad:'1'
},{
  nombre:'Hip thrust',
  cantidad:'1'
},{
  nombre:'Spinning',
  cantidad:'2'
},{
  nombre:'Bicicleta reclinada',
  cantidad:'1'
},{
  nombre:'Sentadilla Sysy',
  cantidad:'1'
},{
  nombre:'Banco predicador',
  cantidad:'1'
}])

//Actualizar 

db.Maquinas.updateOne(
  { nombre: 'Cross over' },
  { $set: { cantidad: '2' } }
);

//Eliminar

db.Maquinas.deleteOne({ nombre: 'Cross over' });

//Consultas

//Cantidad de personas que asistieron en un día específico

db.Asistencia.aggregate([
  {
    $match: {
      dia_asistido: "2026-09-30" // Comparación directa
    }
  },
  {
    $group: {
      _id: { fecha: "$dia_asistido" },
      Personas_que_asistieron_ese_dia: { $sum: 1 }
    }
  }
])

//Cantidad de personas que asistieron en un rango de fechas

db.Asistencia.aggregate([
  {
    $match: {
      dia_asistido: { $gte: "2026-09-01", $lte: "2026-10-02" }
    }
  },
  {
    $group: {
      _id: { fecha: "$dia_asistido" },
      asistencia_de_ese_dia: { $sum: 1 }
    }
  },
  { $sort: { "_id.fecha": 1 } }
])

//Cantidad de veces que un entrenador fue cubierto

db.Entrenadores_Suplentes.aggregate([
  {
    $group: {
      _id: "$e_cubierto.nombre",
      Veces_cubierto: { $sum: 1 }
    }
  },
  {
    $sort: {
      Veces_cubierto: -1
    }
  }
])

//Máquinas que se compraron y su cantidad

db.Maquinas.aggregate([
  {
    $project: {
      _id: 0,
      maquina: "$nombre",
      cantidadComprada: "$cantidad"
    }
  }
])

//Top 5 mancuernas con más cantidad y la cantidad que tienen

db.Mancuernas.aggregate([
  {
    $group: {
      _id: "$peso",
      cantidadTotal: { $sum: "$cantidad" }
    }
  },
  {
    $sort: { cantidadTotal: -1 }
  },
  {
    $limit: 5
  }
])