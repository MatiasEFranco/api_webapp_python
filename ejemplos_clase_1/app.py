'''
Flask [Python]
Ejemplos de clase

Autor: Inove Coding School
Version: 2.0

Descripcion:
Se utiliza Flask para crear un WebServer que levanta los datos de
las personas que registran su ritmo cardíaco.

Ingresar a la siguiente URL para ver los endpoints disponibles
http://127.0.0.1:5000/
'''

from cgitb import text
import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect

# Crear el server Flask
app = Flask(__name__)

# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        # Renderizar el temaplate HTML index.html
        print("Renderizar index.html")
        return render_template('index.html') # aqui importamos el HTML pensado para el ENDPOINT INDEX
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/user
@app.route("/user")
def user():
    try:
        # Renderizar el temaplate HTML user.html
        print("Renderizar user.html")
        return render_template('user.html') # aqui importamos el HTML pensado para el ENDPOINT USER
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/user/<nombre>
@app.route("/user/<name>")
def user_name(name):
    try:
        # Renderizar el temaplate HTML user.html
        print("Renderizar user.html con le nombre", name)
        return render_template('user.html', text=name) # la variable "text" es la que esta dentro de user.html --la informacion la pasamos por la barra de navegacion
    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    print('Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)
