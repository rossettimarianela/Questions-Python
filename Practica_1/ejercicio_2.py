# Escribe un programa que solicite al usuario 
# una cantidad de segundos y muestre
# cuántas horas, minutos y segundos equivalen. 
# Por ejemplo, 3661 segundos son 
# 1 hora, 1 minuto y 1 segundo.

total_seconds = int(input("Ingrese la cantidad de segundos que quiera convertir:  "))

hours = total_seconds // 3600
seconds_left = total_seconds % 3600 #con esto sacamos el resto
minutes = seconds_left // 60
seconds = seconds_left % 60

print(f'{total_seconds} segundos equivalen a {hours} horas, {minutes} minutos y {seconds} segundos.')