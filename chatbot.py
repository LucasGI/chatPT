import json
import re
import datetime
import random
import respuestas_random

LOG_FILE = "lamentos_del_fantasma.txt"

def cargar_json(archivo):
    # En esta funcion se carga el JSON con las palabras clave que pone el usuario en su input y las respuestas a estas.
    with open(archivo, encoding="utf-8") as respuesta_bot:
        return json.load(respuesta_bot)
    
data_respuestas = cargar_json("respuestas.json")



def guardar_lamento(texto):
    #esta funcion guarda en el archivo txt toda la conversaqcion que vas teniendo con el bot
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {texto}\n")





def responder(pregunta):
    """ Estas funcion  es la encargada de leer el input que esta poniendo el usuario, separar las palabras agregadaa y las toma 
    como palabras clave. Si una de esas palabras clave coincide con las del JSON cargado anteriormente, suma un "punto" en esa
    respuesta. La respuesta que tenga mas puntos es la que se va a mostrar. """
    pregunta = re.split(r'\s+|[,;?!.-]\s*', pregunta.lower().strip())
    puntajes = []

    for respuesta in data_respuestas:
        puntaje = 0
        palabras_clave = respuesta["input_usuario"]

        for palabra in pregunta:
            if palabra in palabras_clave:
                puntaje += 1

        puntajes.append(puntaje)

    mejor_puntaje = max(puntajes)
    
    # Si el input esta vacio muestra este mensaje
    if pregunta == "":
        return "El silencio también compila… y yo escucho cada bit del vacío."
    
    """ Si no se encuentra ninguna palabra clave se muestra una de las respuestas aleatorias de "respuestas_random.py" en donde ya
    fue seleccionada anteriormente por la funcion que hay adentro de ese archivo"""
    if mejor_puntaje == 0: 
        return respuestas_random.random_string()
    

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







print("👻 El Fantasma del Verso Eterno 👻")
print("Háblale... o abandona este lugar (escribe 'salir')")
while True:
    entrada = input("Tú: ")
    if entrada.lower() == "salir":
        print("El fantasma se desvanece entre sombras y líneas de código...")
        break
    respuesta = responder(entrada)
    print("Fantasma:", respuesta)