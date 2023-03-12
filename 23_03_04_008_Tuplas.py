#Alan de Jesus Fabian Garcia 04/03/23
#Crear y manejar tuplas capitulo 19 
lista = ['rojo', 'azul', 'verde', 'amarillo']
tupla = ('rojo', 'azul', 'verde', 'amarillo')#tuplas se manejar con parentesis 
print(tupla)
#acceder a posiciones dentro de tuplas
print(tupla[0])
#datos soportados en tuplas
tupla = (10, 15, 20, 'El resultado de la operación es:')
print(tupla[3], tupla[2] + tupla[0] * tupla[1] / tupla[0])
#Ejercicios de python 
#33imprime la segunda posicion de esta tupla
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(colores[1])
#34 Utiliza los símbolos de suma y resta para obtener el resultado 25 a partir de los elementos de la siguiente tupla en una variable llamada operacion.
numeros = (10, 1, 5, 11)
operacion = numeros[0] + numeros[2] + numeros[3] - numeros[1]
print(operacion)
#como convertir de tuplas a listas y viceversa cap 20
lista =['rojo','azul','verde','amarillo']
tupla = tuple(lista)
print(type(tupla))
# 35.Convierte la siguiente lista en una tupla y asegúrate que se haya convertido en tupla correctamente imprimiendo en la consola el tipo de elemento que es.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores_tupla =tuple(colores)
print(type(colores_tupla))