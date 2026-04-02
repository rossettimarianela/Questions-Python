# Crea un programa que dado un número N 
# ingresado por el usuario, imprima los
# números del 1 al N pero saltee los 
# múltiplos de 5. Nota: utilizá la sentencia continue
# Entrega donde haga falta.

number = int(input("Ingrese un numero limite: "))
for i in range(1,number+1):
    if i % 5 == 0: # Si es multiplo de 5 hago un continue
        continue
    print(i, end=", ")