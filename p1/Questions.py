import random
import sys
 # Preguntas para el juego
questions = [
 "¿Qué función se usa para obtener la longitud de una cadena en Python?",
 "¿Cuál de las siguientes opciones es un número entero en Python?",
 "¿Cómo se solicita entrada del usuario en Python?",
 "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
 "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
 ]
 # Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
 ("size()", "len()", "length()", "count()"),
 ("3.14", "'42'", "10", "True"),
 ("input()", "scan()", "read()", "ask()"),
 (
 "// Esto es un comentario",
 "/* Esto es un comentario */",
 "-- Esto es un comentario",
 "# Esto es un comentario",
 ),
 ("=", "==", "!=", "==="),
 ]
 # Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3) #ahora no se pueden repetir
#combina en una lista de tuplas, las preguntas, las opciones y las respuestas
puntaje = 0
# El usuario deberá contestar 3 preguntas
for preguntas,opciones,respuestas in questions_to_ask:
 # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions)-1)
 # Se muestra la pregunta y las respuestas posibles
    print(preguntas)
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
 # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: ")) #modificacion: quitar el int en el input y sacar el -1
        if user_answer.isnumeric()==False: #si la respuesta no es un número muestre un mensaje diciendo: "Respuesta no válida"
            print("Respuesta no válida")
            sys.exit() #termine de inmediato con exit status
        else:
            user_answer = int(user_answer)-1 #convertir a int. ya sabiendo que es numerico y restarle uno para obtener la respuesta real
            if(user_answer < 0) or (user_answer > 3): #si la respuesta no esta en el rango de las respuestas posibles muestre un mensaje diciendo: "Respuesta no válida"
                print("Respuesta no válida")
                sys.exit() #termine de inmediato con exit status
 # Se verifica si la respuesta es correcta
            elif user_answer == respuestas:
                print("¡Correcto!")
                puntaje+=1 #si es correcto, sumo 1 al puntaje
                break
            else:
 # Si el usuario no responde correctamente después de 2 intentos,
 # se muestra la respuesta correcta
                print("Incorrecto. La respuesta correcta es:")
                print(opciones[respuestas])
                puntaje -= 0.5 #si es incorrecto, resto 0,5 al puntaje
                break
 # Se imprime un blanco al final de la pregunta
    print()
if(puntaje>0):
    print(f"puntaje: {puntaje}")
else:
    print("El puntaje fue menor o igual a 0 :(")
