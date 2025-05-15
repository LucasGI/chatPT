import funciones

data_respuestas = funciones.cargar_json("respuestas.json")

"""El bot se presenta previo a la primera interaccion del usuario con el"""

print("👻 El Fantasma del Verso Eterno 👻")
print("Saludos, alma errante... Soy PyGhost, susurro de lo que fue, sombra de lo que aún vibra entre los velos del tiempo.")
print("Podemos tener una charla trivial, de hola, como estas, podes preguntarme que o quien soy o podes pedirme algo mas especifico, \ncomo que te escriba un poema, responda tus dudas sobre el futuro, el amor, los deseos, el miedo u otras cuestiones")
print("\nHablame... o abandona este lugar (escribe 'salir')")


""" Dentro de este while se llama a las funciones que hacen posible la charla con el bot. solamente input para levantar la pregunta y print para mostrar la respuesta generada """
while True:
    entrada = input("Tú: ")
    if entrada.lower() == "salir" or entrada.strip() == "":
        confirmar = input("¿Estás seguro de que quieres salir? (s/n): ").strip().lower()
        if confirmar == "s":
            print("El fantasma se desvanece entre sombras y líneas de código...")
            break
        else:
            print("El conjuro continúa... de que quieres hablar? ")
            continue
    respuesta = funciones.responder(entrada, data_respuestas)
    print("PyGhost:", respuesta)
