
import random

words = [
"python",
"programa",
"variable",
"funcion",
"bucle",
"cadena",
"entero",
"lista",
]

word = random.choice(words)
guessed = []
attempts = 6
score = 0

print()
print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        score += 6
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ").lower()

    # Verifico si la letra es de 1 solo caracter y si es una letra
    if len(letter) != 1 or letter not in "abcdefghijklmnopqrstuvwxyz":
        print("Entrada no válida")
    elif letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        score -= 1
        print("Esa letra no está en la palabra.")
    print()

else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0

print(f'Puntaje Obtenido: {score}')



'''El juego tiene un bug. Si el usuario ingresa más de una letra, un número o cualquier
otro carácter inválido, el programa se comporta de manera inesperada.
Modificalo para que en ese caso muestre el mensaje "Entrada no válida" y continúe el juego 
en la siguiente iteración '''


'''Modificá el juego para que al final de la partida se muestre el puntaje del jugador. 
El puntaje se calcula de la siguiente forma: cada letra incorrecta resta 1 punto,
adivinar la palabra completa suma 6 puntos, y perder deja el puntaje en 0.'''