# Modifica el ejercicio 4 para que, en lugar de imprimir los números, 
# genere dos listas:
# una con los múltiplos de 5 y otra con el resto de los números. 
# Imprimí ambas listas al finalizar.

multiples_of_five = []
numbers = []

number = int(input("Ingrese un numero limite: "))
for i in range(1,number+1):
    if i % 5 == 0: 
        multiples_of_five.append(i)
        continue
    numbers.append(i)
print(f'Lista de los numeros multiples de 5: {multiples_of_five}')
print(f'Lista del resto de numeros: {numbers}')