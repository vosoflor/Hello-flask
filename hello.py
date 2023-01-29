from flask import Flask, render_template

# Inicializar librería
app = Flask(__name__)

# Recordar que el @ es decorador, con ésta línea se define la ruta donde vamos a estar ejecutando la función que sigue
@app.route("/hola")

def hola_mundo():
    return ("Hola mundo flask")

'''
Al ejecutar lo anterior Flask trabajará en su propio servidor en donde programaremos las rutas definidas como /hola
y las transformará en peticiones HTTP (esto significa que se van a ejecutar en la web). Cuando se haga una ejecución
de manera local entonces la dirección sería: http://localhost/...
'''

# Ejercicio 1
@app.route("/adios")

def despedida():
    return ("Hasta pronto Verónica!!!")

# Ejemplo para enviar parámetros en las rutas (la variable en la ruta debe tener el mismo nombre de la variable de la función)
@app.route("/nombre/<n>")

def name(n):
    return f"Tu nombre es {n}"

# Ejercicio 2
@app.route("/cuadrado_del_numero/<value>") # También se podría definir "/cuadrado_del_numero/<int:value>" para que obligue a recibir números enteros
# lo anterior significa que podemos asignar el tipo del párámetro en la ruta ya sea int, float, str

def square(value):
    n = int(value)
    return f"El cuadrado del número {n} es {n*n}"

# Ejercicio 3
@app.route("/operaciones/<ope>/<float:n1>/<float:n2>")

def calculadora(ope, n1, n2):
    if ope == "suma":
        return f"La suma es {n1+n2}"
    elif ope == "resta":
        return f"La resta es {n1-n2}"
    elif ope == "multiplicación":
        return f"La multiplicación es {n1*n2}"
    elif ope == "división":
        return f"La división es {n1/n2}"

# Ejemplo de cómo devolver un HTML por Flask
@app.route("/primerhtml/<nombre>")

def callhtml(nombre):
    return render_template("hola.html", name = nombre)