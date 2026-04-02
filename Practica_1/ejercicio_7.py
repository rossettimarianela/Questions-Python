# Escribe un programa que solicite al usuario una lista de palabras. 
# Luego, construí una oración uniendo únicamente las palabras que 
# tengan más de 3 letras, separadas por espacios.
# Las palabras cortas deben ser excluidas del resultado final.

words = input("Ingrese palabras separadas por espacios: ").split()
words_greater_than_3 = []
for word in words:
    if len(word) > 3: 
        words_greater_than_3.append(word)
sentence= " ".join(words_greater_than_3)
print(f'Oración formada: {sentence}')
