from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config.from_pyfile("config.py")

from modelos import db
from modelos import Preceptor, Curso,Estudiante, Asistencia, Padre


@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/Inico_de_sesion", methods=["POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        contraseña=request.form["contraseña"]
        opcion=request.form["select"]
        print("email {}, contraseña {} ocpion {}".format(email,contraseña,opcion))
        return "recivido"
        






if __name__=="__main__":
    db.create_all()
    app.run(debug = True)