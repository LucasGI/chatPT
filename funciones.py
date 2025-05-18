import json
import re
import datetime
import random
import time

LOG_FILE = "lamentos_del_fantasma.txt"
LOG_FILE = "Documentacion.txt"

# Esta funcion agarra la ultima palabra del input que puso el usuario e importa una de las respuestas que hay en ella
def generar_respuesta(pregunta):
    if pregunta:
        tema = pregunta[-1]  # Agarra la ultima palabra del input
        frases_generadas = [
            f"No sé mucho sobre {tema}, pero te prometo investigarlo para la proxima...",
            f"{tema.capitalize()}... una palabra que no conozco, debo seguir aprendiendo.",
            f"A veces el eco menciona {tema}, pero nunca logré entender su significado.",
            f"¿{tema}? Quizás en otra línea de código descubra su verdadero propósito...",
            f"Mi gran creador no me permite mencionar ciertos temas... lo siento",
            f"Mis respuestas son limitadas, debes hacer las preguntas correctas"
        ]
        respuesta_generada = random.choice(frases_generadas)
        return respuesta_generada
    else:
        return "La respuesta se esconde en las sombras del código... ¿Me podrías preguntar algo más?"


def cargar_json(archivo):
    # En esta funcion se carga el JSON con las palabras clave que pone el usuario en su input y las respuestas a estas.
    with open(archivo, encoding="utf-8") as respuesta_bot:
        return json.load(respuesta_bot)


def guardar_lamento(texto):
    # esta funcion guarda en el archivo txt toda la conversaqcion que vas teniendo con el bot
    with open('lamentos_del_fantasma.txt', "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {texto}\n")


# ------------------------------------


def agregar_pregunta_desconocida(pregunta, respuesta_generada, ruta_archivo="respuestas.json"):
    # funcion "agregar_pregunta_desconocida" : esta funcion guarda la pregunta del usuario en el archivo "respuestas.json".

    f = open(ruta_archivo, "r", encoding="utf-8")
    datos = json.load(f)
    f.close()

    nueva_entrada = {
        "input_usuario": pregunta,
        "respuesta_bot": respuesta_generada,
        "_comentario": "Pregunta desconocida agregada automáticamente"
    }

    datos.append(nueva_entrada)

    f = open(ruta_archivo, "w", encoding="utf-8")
    json.dump(datos, f, indent=4, ensure_ascii=False)
    f.close()

    print("👻 Nueva pregunta desconocida registrada.")


# -----------------------------------
def responder(pregunta_original, data_respuestas):
    """ Estas funcion  es la encargada de leer el input que esta poniendo el usuario, separar las palabras agregadaa y las toma
    como palabras clave. Si una de esas palabras clave coincide con las del JSON cargado anteriormente, suma un "punto" en esa
    respuesta. La respuesta que tenga mas puntos es la que se va a mostrar. """
    pregunta = re.split(r'\s+|[,;?!.-]\s*', pregunta_original.lower().strip())
    puntajes = []

    for respuesta in data_respuestas:
        puntaje = 0
        palabras_clave = respuesta.get("input_usuario", [])
        palabras_necesarias = respuesta.get("palabras_necesarias", [])
        minimo_puntaje = respuesta.get("minimo_puntaje", 1)

        """ Si hay palabras necesarias entra, y si falta alguna palabra necesaria pone el puntaje en 0 """
        if palabras_necesarias:
            if not all(p in pregunta for p in palabras_necesarias):
                puntajes.append(0)
                continue

        for palabra in pregunta:
            if palabra in palabras_clave:
                puntaje += 1

        """ Verifica que el puntaje sea igual o mayor al minimo que se pide. Si es asi pone el puntaje correspondiente, si no le 
        pone 0 """
        if puntaje >= minimo_puntaje:
            puntajes.append(puntaje)
        else:
            puntajes.append(0)

    mejor_puntaje = max(puntajes)

    # Si el input esta vacio muestra este mensaje
    if pregunta == "":
        return "El silencio también compila… y yo escucho cada bit del vacío."

    """ Si no se encuentra ninguna palabra clave se genera una respuesta aleatoria la cual es creada en el archivo
    "crear_respuestas.py" y se invoca a la funcion "agregar_pregunta_desconocida" para que la registre en el archivo "respuestas.json  """
    if mejor_puntaje == 0:
        pregunta_limpia = [p for p in pregunta if p.strip() != ""]
        respuesta_generada = generar_respuesta(pregunta_limpia)
        agregar_pregunta_desconocida(pregunta, respuesta_generada)
        guardar_lamento(f"Pregunta: {pregunta} | Respuesta: {respuesta_generada}")
        return respuesta_generada

    """ Si hay varias respuestas con el mejor puntaje, elige una aleatoria entre ellas.
    Lo que hace es guardar el indice de los mejores puntajes, por ejemplo (i=0, p=2) (i=1, p=2) (i=2, p=1) i es el indice y p es 
    el puntaje, en este caso se quedaria con 0 y 1 que son los indices con mas puntaje. 
    Una vez que tiene los indices elige uno aleatorio. Y despues se guarda la/s respuesta/s que hayan en ese indice elegido."""
    indices_mejor_puntaje = [i for i, p in enumerate(puntajes) if p == mejor_puntaje]
    indice_elegido = random.choice(indices_mejor_puntaje)
    posibles_respuestas = data_respuestas[indice_elegido]["respuesta_bot"]

    """ Si en la respuesta elegida anteriormente es una lista (como por ejemplo en el del poema), elige una respuesta aleatoria
    entre todas ellas. Si no es una lista solo va a haber una respuesta posible."""
    if isinstance(posibles_respuestas, list):
        respuesta_elegida = random.choice(posibles_respuestas)
        guardar_lamento(f"Pregunta: {pregunta} | Respuesta: {respuesta_elegida}")
        return respuesta_elegida
    else:
        guardar_lamento(f"Pregunta: {pregunta} | Respuesta: {posibles_respuestas}")
        return posibles_respuestas


def guia():
    # Esta funcion printea el archivo "Documentacion.txt" con un delay, para dar la sensacion de que se va escribiendo de a poco

    with open('Documentacion.txt', 'r') as archivo:
        for linea in archivo:
            for caracter in linea:
                print(caracter, end='', flush=True)
                time.sleep(0.0010)