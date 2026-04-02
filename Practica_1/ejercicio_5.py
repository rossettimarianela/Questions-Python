# Escribe un programa que simule una caja registradora: 
# el usuario ingresa precios de
# productos de a uno. Cuando ingresa 0, el programa se detiene 
# y muestra el total acumulado. 
# Nota: utilizá la sentencia break cuando haga falta.

print("Ingrese los precios de los productos (0 para finalizar): ")
total_prices= 0.0

while True:
    price = float(input("Precio del producto: $"))
    if price == 0: break
    if price < 0: 
        print("Valor no válido")
        continue
    total_prices += price
print(f'El total de los productos es: {total_prices}')

