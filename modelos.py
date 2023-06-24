from __main__ import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)
app.app_context().push()

class Preceptor(db.Model):
    __tablename__= "preceptor"
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    correo = db.Column(db.String(120),unique=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)

class Padre(db.Model):
    __tablename__= "padre"
    idPadre = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    correo = db.Column(db.String(120),unique=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)

class Curso(db.Model):
    __tablename__="curso"
    idCurso = db.Column(db.Integer, primary_key= True)
    anio = db.Column(db.Integer, primary_key= True)
    division = db.Column(db.Integer, primary_key= True)
    idpreceptor = db.Column(db.Integer, db.ForeignKey("preceptor.id"))


class Estudiante(db.Model):
    __tablename__="estudiante"
    idEstudiante = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    dni = db.Column(db.String(120), nullable=False)
    IDcurso = db.Column(db.Integer, db.ForeignKey("curso.idCurso"))
    IDpadre = db.Column(db.Integer, db.ForeignKey("padre.idPadre"))


class Asistencia(db.Model):
    __tablename__="asitencia"
    idAsistencia = db.Column(db.Integer, primary_key
    = True)
    fecha = db.Column(db.DateTime, nullable=False)
    codigoClase = db.Column(db.Integer, nullable=False)
    asistio = db.Column(db.Boolean, nullable=False)
    custificacion = db.Column(db.String(120),nullable=False)
    IDEstudiante = db.Column(db.Integer, db.ForeignKey("estudiante.idEstudiante"))

    
    