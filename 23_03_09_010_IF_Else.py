#Alan de Jesus Fabian Garcia 09/03/23
#Ejemplo capitulo 22
edad = 20
if edad >= 18:
	print('Puedes acceder, eres mayor de edad.')
else:
	print('No puedes acceder, eres menor de edad.')

edad = 15
if edad >= 18:
    print('Puedes acceder,eres mayor de edad')
else:
    print('No puedes acceder,eres menos de edad')

#Ejercicios de python 
#39 Corrige el siguiente condicional if else
color = 'rojo'
if color == 'rojo':
    print("El color es rojo")
else  :
    print("El color no es rojo ")
#Ejemplo capitulo 23
edad= int(input('¿Cual es tu edad? \n'))
if edad<=0:
    print('nadie puede tener esa edad.')
elif edad <= 1 and edad <=18:
    print('eres menor de edad.')
elif edad >= 18 and  edad <=100:
    print('Eres mayor de edad.')
else:
    print('Edad no valida.')
#Ejercicios de python 
#40.Al siguiente codigo añadele un par de rangos de edad.uno de 18 años hasta 45 y otro mas de 100 años hasta 120
edad = int (input('¿Cual es tu edad?\n'))
if edad <= 0:
    print('Nadie puede tener esa edad.')
elif edad>=1 and edad<=18:
    print('Eres menor de edad.')
elif edad>=18 and edad<=45:
    print('Estas entre la juventud y la crisis de los 40')
elif edad>=45 and edad<=100:
    print('Eres mayor de edad')
elif edad>=100 and edad<=120:
    print('Ya clasificas como reliquia de la humanidad')
else:
    print('Edad no valida')
#Capitulo 24 Ejemplo

entrada = int(input('Introduce un número del 1 al 4:\n'))

if entrada == 1:
    print('Has seleccionado la opción número 1.')
if entrada == 2:
    print('Has seleccionado la opción número 2.')
if entrada == 3:
    print('Has seleccionado la opción número 3.')
if entrada == 4:
    print('Has seleccionado la opción número 4.')
#Ejercicios python
