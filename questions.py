
import random

categories = {
    "Programacion":["python","programa","variable","funcion","bucle","cadena","entero","lista"],
    "Animales":["perro", "gato", "tortuga", "elefante", "orca", "delfin", "cangrejo", "yaguarete"],
    "Colores": ["amarillo", "azul", "verde", "rosa", "naranja", "turquesa", "fucsia", "rojo", "magenta" ],
    "Objetos": ["libro","mesa","cartera","sillon","tenedor","lampara","zapatilla","ventana"]
}

""" words = ["python","programa","variable","funcion","bucle","cadena","entero","lista",] """

print()
print("¡Bienvenido al Ahorcado!")
print()

# Menu de categorias
print("Categorias disponibles: ")
for category in categories:
    print(f'- {category}')
while True:
    option = input("Elegí una categoria: ").capitalize()
    if option in categories:
        break
    else:
        print("Categoria no válida, intentá de nuevo.")

# random.sample toma la lista de palabras de la categoria y devuelve
# todas mezcladas al azar, sin repetir ninguna
words = random.sample(categories[option], len(categories[option]))
word = words[0]

guessed = []
attempts = 6
score = 0


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

'''Modificá el juego para que las palabras estén agrupadas por categoría.
Al inicio de cada partida, mostrar las categorías disponibles y permitir que el usuario
elija una. Ayuda: utilizá un diccionario donde las claves sean los nombres de las
categorías y los valores sean listas de palabras.'''

'''Modificá el juego para que, al jugar varias rondas seguidas, no se repita la misma
palabra. Investigá la función random.sample()'''