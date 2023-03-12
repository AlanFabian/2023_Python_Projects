#Alan de Jesus Fabian Garcia 10 de marzo de 2023
#Ejemplo capitulo 29
for x in 'Python':
    print(x)
#Iterar en cada ciclo una letra de la cadena de texto Python
#Iteracion en listas
cursos = ['Python', 'JavaScript', 'COBOL', 'HTML']

for x in cursos:
	print(x)
#Bucle vacio con un pass
for x in '':
	pass
#Ejercicios Python
#46Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'.
colores = ('rojo', 'azul', 'verde', 'amarillo')

for x in colores:
	print('El color es: ' + x + '.')
#Ejemplo Capitulo 30 tipo de dato range 
for x in range(10):
	print(x)
#Especificar un segundo parametro
for x in range(5,10):
	print(x)
#Para especificar un incremento o decremento se puede aplicar un tercer parametro teniendo que ser este un numero positivo o negativo
for x in range(10, -500, -50):
	print(x)
#Ejercicios de python
#47 Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. Basta con que imprimas el valor de cada iteración.
#El maximo calor obtenido antes de que se salga del rango que debemos utilizar es 607
for x in range(7, 700, 100):
	print(x)
