from flask import Flask
from flask import render_template as render
from flask import redirect
from flask import request
from flask.templating import render_template
import json

app = Flask(__name__)

lista_usuarios = {
    123: {"nombre": "Andres", "rol": "admin"},
    234: {"nombre": "Andres", "rol": "medico"},
    345: {"nombre": "Andres", "rol": "usuario"},
}

lista_noticias = {
    234: {
        "autor": 123,
        "titulo": "Noticia 2",
        "cuerpo": " 2 2 2 2 2 2 2 2",
        "imagenes": ["img 1", "img 1", "img 1"],
    },
    345: {
        "autor": 123,
        "titulo": "Noticia 3",
        "cuerpo": " 3 3 3 3 3 3 3 3",
        "imagenes": ["img 1", "img 1", "img 1"],
    },
    567: {
        "autor": 123,
        "titulo": "Noticia 4",
        "cuerpo": " 4 4 4 4 4 4 4 4",
        "imagenes": ["img 1", "img 1", "img 1"],
    },
    678: {
        "autor": 123,
        "titulo": "Noticia 5",
        "cuerpo": " 5 5 5 5 5 5 5 5",
        "imagenes": ["img 1", "img 1", "img 1"],
    },
}


sesion_iniciada = False


@app.route("/agregar_noticia", methods=["POST"])
def agregar_noticia():
    # Leer información de nueva noticia
    nueva_noticia = (
        {
            "autor": 123,
            "titulo": "Noticia 2",
            "cuerpo": " 2 2 2 2 2 2 2 2",
            "imagenes": ["img 1", "img 1", "img 1"],
        },
    )
    lista_noticias[len(lista_noticias)] = nueva_noticia

    return redirect("/ingreso")


@app.route("/eliminar_noticia/<id_noticia>", methods=["GTET"])
def eliminar_noticia(id_noticia):
    if id_noticia in lista_noticias:
        del lista_noticias[id_noticia]
    return redirect("/")


@app.route("/", methods=["GET"])
@app.route("/inicio", methods=["GET"])
def inicio():
    # Si ya inició sesión -> Lista de noticias
    # Sino -> Bienvenida -> 4 o 5 html terminados (pero basicos)
    return render(
        "inicio.html",
        sesion_iniciada=sesion_iniciada,
        lista_noticias=lista_noticias,
        user=lista_usuarios[123],
    )


@app.route("/registro", methods=["GET", "POST"])
def registro():
    return "Pagina de registro"


@app.route("/ingreso", methods=["GET", "POST"])
def ingreso():
    global sesion_iniciada
    if request.method == "GET":
        if sesion_iniciada:
            return redirect("/inicio")
        else:
            return render("ingreso.html")
    else:
        # Aqui se debe hacer la validacion
        sesion_iniciada = True
        return redirect("/inicio")


@app.route("/salir", methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect("/inicio")


@app.route("/perfil", methods=["GET", "POST"])
def perfil():
    return "Pagina de perfil de usuario"


@app.route("/usuario/<id_usuario>", methods=["GET"])
def usuario_info(id_usuario):
    if id_usuario in lista_usuarios:
        return f"Estás viendo el perfil del usuario: {id_usuario}"
    else:
        return f"Error el usuario {id_usuario} no existe"


@app.route("/usuario/<id_usuario>/amigos", methods=["GET"])
def usuario_info_amigos(id_usuario):
    if id_usuario in lista_usuarios:
        return f"Estás viendo el perfil del usuario: {id_usuario}"
    else:
        return f"Error el usuario {id_usuario} no existe"


@app.route("/noticia/<id_noticia>", methods=["GET"])
def noticia_detalle(id_noticia):
    try:
        id_noticia = int(id_noticia)
    except Exception as e:
        id_noticia = 0

    if id_noticia in lista_noticias:
        return lista_noticias[id_noticia]
    else:
        return f"La noticia que estás buscando ({id_noticia}) no existe en nuestra base de datos"


if __name__ == "__main__":
    app.run(debug=True)
