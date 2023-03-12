#Alan de Jesus Fabian Garcia 10 de marzo de 2023
#Ejemplo capitulo 27
#Bucle while infinito
x = 1

while x < 10:
	print(x)
#Incrementar o decrementar bucles while 
x = 1

while x < 10:
	print(x)
	x += 1

x = 9
#Decremento
while x > 0:
	print(x)
	x -= 2
#Ejercicios python
#42 Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
#para solucionarlo deberiamos poner el operador<= e incrementar de 5 en 5 en cada ciclo
x = 0

while x <= 15:
	print(x)
	x += 5

#43 Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
#invirtiendo el operador y utilizando decrementos podremos llegar a -100
x = 0

while x >= -100:
	print(x)
	x -= 20
#Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'...
#se va decrementando y con el print ir concatenando una frase con el valor de x
x = 10

while x >= 0:
	print('El valor de x es: ', x)
	x -= 1

#Capitulo 28
#Bucles if anidados dentro del while
x = 1

while x <= 10:
	print(x)
	if x == 5:
		break
	x += 1
#Aplicar saltos dentro del bucle while
x = 0

while x < 10:
	x += 1
	if x == 5 or x == 7:
		continue
	print(x)
#Ejercicio python
#45Crea un bucle while con las siguientes características:El valor inicial de la variable x será de 0.
#El valor de incremento será 1.
#La condición de salida del bucle será mayor o igual a 30.
#La ejecución se deberá romper cuando x valga 15.
#Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x.
# Valor inicial de x
x = 0

# while se ejecuta hasta que  es menor o igual que 30
while x <= 30:
	x += 1  # incrementos de 1

	# if para saltar ejecuciones del bucle
	if x == 4 or x == 6 or x == 10:
		print('Se saltó el valor ', x, ' de x')
		continue

	# if para romper la ejecución del bucle
	if x == 15:
		print('Se rompió la ejecución del bucle cuando x valía: ', x)
		break

	# imprime los resultados que no se corresponden a ninguno de los if
	print(x)

