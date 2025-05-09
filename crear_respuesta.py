import random


# Esta funcion agarra la ultima palabra del input que puso el usuario e importa una de las respuestas que hay en ella
def generar_respuesta(pregunta):
    if pregunta:  
        tema = pregunta[-1]  # Agarra la ultima palabra del input
        frases_generadas = [
            f"No sé mucho sobre {tema}, pero suena como algo digno de un conjuro...",
            f"{tema.capitalize()}... una palabra que retumba en los pasillos de la memoria perdida.",
            f"A veces el eco menciona {tema}, pero nunca logré entender su significado.",
            f"¿{tema}? Quizás en otra línea de código descubra su verdadero propósito...",
            f"Mi gran creador no me permite mencionar ciertos temas... lo siento",
            f"Mis respuestas son limitadas, debes hacer las preguntas correctas"
        ]
        respuesta_generada = random.choice(frases_generadas)
        return respuesta_generada
    else:
        return "La respuesta se esconde en las sombras del código... ¿Me podrías preguntar algo más?"