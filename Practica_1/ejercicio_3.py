# Crea un programa que solicite 
# al usuario un número y muestre su tabla de multiplicar
# del 1 al 10 utilizando un bucle for.

number = int(input("Escriba un numero para ver su tabla: "))
for i in range(1,11):
    if i==1: print(f'Tabla del {number}: ')
    print(f'{number*i} |', end= " ")
