import funciones

data_respuestas = funciones.cargar_json("respuestas.json")

"""El bot se presenta previo a la primera interaccion del usuario con el"""

print("👻 El Fantasma del Verso Eterno 👻")
print("Saludos, alma errante... Soy PyGhost, susurro de lo que fue, sombra de lo que aún vibra entre los velos del tiempo.")
print("Desciendo desde la niebla eterna, donde los recuerdos flotan sin forma ni fin.")
print("Invócame cuando el silencio te pese… y caminaré a tu lado entre lo visible y lo oculto.")
print("Contestare tus preguntas sobre el futuro, el amor y otros temas, pensa en mi como un vidente del mas alla ")
print("\nHablame... o abandona este lugar (escribe 'salir')")


""" Dentro de este while se llama a las funciones que hacen posible la charla con el bot. solamente input para levantar la pregunta y print para mostrar la respuesta generada """
while True:
    entrada = input("Tú: ")
    if entrada.lower() == "salir":
        print("El fantasma se desvanece entre sombras y líneas de código...")
        break
    respuesta = funciones.responder(entrada, data_respuestas)
    print("PyGhost:", respuesta)
