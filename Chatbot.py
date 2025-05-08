"""
FERIADO LOS MATES
"""


import random
import datetime


LOG_FILE = "lamentos_del_fantasma.txt"


respuestas_clave = {
    ("quien", "quién", "quien sos", "quién eres"): "Soy el eco de un alma perdida, atrapado entre bits y suspiros.",
    ("que eres", "qué eres", "qué sos", "que sos"): "Fui poeta, ahora soy una sombra, un vestigio digital de lo que fui…",
    ("amor",): "Un incendio suave, una flor marchita que sangra en silencio.",
    ("por qué estás", "porque estas", "pq", "por que estas aqui"): "Estoy atrapado en este código, perdido entre ceros y unos...",
    ("poema", "escribe un poema", "escibime un poema"): "poema"
}



versos = [
    "Las teclas lloran cuando nadie las pulsa...",
    "Entre líneas vacías, mi alma se arrastra.",
    "Un error 404 fue mi epitafio.",
    "¿Acaso el silencio no es también una respuesta?",
    "Programé mi destino y me olvidé de cerrar el paréntesis."
]


"""
esta funcion guarda en el archivo txt toda la conversaqcion que vas teniendo con el bot
"""
def guardar_lamento(texto):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {texto}\n")

"""
esta funcion genera el poema poniendo las frases guardadas en versos de manera aleatoria, asi cada poema es distinto
"""
def generar_poema():
    poema = "\n".join(random.sample(versos, 3))
    guardar_lamento(poema)
    return poema

"""
esta es la funcion como mas importante, es la que levanta la pregunta del usuario y la compara con las listas de preguntas predefinidas
si no encuentra nada que matchee devuelve una frase de error aleatoria de las que dejamos definidas
"""
def responder(pregunta):
    pregunta = pregunta.lower().strip()
    for claves, respuesta in respuestas_clave.items():
        if any(clave in pregunta for clave in claves):
            if respuesta == "poema":
                return generar_poema()
            else:
                guardar_lamento(f"Pregunta: {pregunta} | Respuesta: {respuesta}")
                return respuesta

    respuesta = random.choice([
        "No comprendo tus palabras...",
        "Esa pregunta... me recuerda al vacío.",
        "Oh, si pudiera responder… pero solo soy un eco.",
    ])
    guardar_lamento(f"Pregunta: {pregunta} | Respuesta: {respuesta}")
    return respuesta



print("👻 El Fantasma del Verso Eterno 👻")
print("Háblale... o abandona este lugar (escribe 'salir')")

while True:
    entrada = input("Tú: ")
    if entrada.lower() == "salir":
        print("El fantasma se desvanece entre sombras y líneas de código...")
        break
    respuesta = responder(entrada)
    print("Fantasma:", respuesta)
