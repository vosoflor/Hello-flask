# Aplicación de intrudcción a Flask

Programa hecho en Python con framework Flask, el famoso "Hello World".

# Instalación

En su entorno de Python ejecutar el comando:

```
pip install -r requirements.txt
```

La librería utilizada es Flask (https://flask.palletsprojects.com/en/2.2.x/quickstart/).

# Ejecución del programa

1. Comando para inicializar el servidor del programa:
    
    en mac ```export FLASK_APP=hello.py```
    en windows ```set FLASK_APP=hello.py```

2. Comando para ejecutar el servidor:

    ```
    flask --app hello run
    ```

    Al ejecutar el servidor aparece la ruta que en este caso sería el localhost http://127.0.0.1:5000.

    El 5000 es un puerto, si se observa la ruta en un navegador aparece el mensaje URL not found on the server
    pero si se adiciona /hola que fue la ruta asignada en el programa entonces vamos a observar en la web la ejecución del programa.

3. Comando para ejecutar el servidor pero haciendo actualizaciones de código en tiempo real:

    ```
    flask --app hello --debug run
    ```

4. Comando especial para lanzar el servidor en un puerto diferente. Ésto se utiliza en los casos que el puerto 5000 esté ocupado.

    El servidor no toma los ajustes del código en tiempo real por lo que para cada ajuste se debe salir de ejecución y volver a
    ejecutar para que tome los cambios a menos que se utilice el siguiente comando:
    
    ```
    flask --app hello run -p 5001
    ```