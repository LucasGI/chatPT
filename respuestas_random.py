import random

def random_string():
    #esta funcion tiene varias respuestas para cuando el bot no sepa que responder, y manda una de las respuestas al archivo principal
    respuestas = [
        "No comprendo tus palabras...",
        "Esa pregunta... me recuerda al vacío.",
        "Oh, si pudiera responder… pero solo soy un eco.",
    ]
    return random.choice(respuestas)