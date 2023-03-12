#Alan de Jesus Fabian Garcia 11 de marzo de 2023
#Ejemplo capitulo 31
#Creacion de diccionarios 
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

consulta = teclado1['Modelo']
print(consulta)
#Para imprimir un diccionario python entero 
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

print(teclado1)
#Ejercicios python 
#48.Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print(). El resultado será esto en la consola: El modelo Corsair K55 RGB cuesta 59,99 $.
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

print('El modelo', teclado2['Modelo'], 'cuesta', teclado2['Precio'], '$.')
#Ejemplo capitulo 32 usar diccionarios con el bucle for 
#Modificar el valor a 'Precio'
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

teclado1['Precio'] = '85'
print(teclado1['Precio'])
#Iterar  en un diccionario en python aplicando un bucle for 
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x in teclado2:
	print(x)
#Iterar en un diccionario para devolver sus valores 
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x in teclado2:
	print(teclado2[x])
#Ejercicios python 
#49 Itera el diccionario teclado1 con un solo bucle for que muestre esto en consola:
# Categoría = Teclados.
#Modelo = HyperX Alloy FPS Pro.
#Precio = 89,99.
#Solo se aplican los dos ejemplos el de iteracciones con un ciclo for y buscando devolver los valores del diccionario 
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

for x in teclado1:
	print(x, '=', teclado1[x] + '.')
#Ejemplo capitulo 33
teclado = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

print(len(teclado))
#Con el metodo len podemos contar la longitud de los elementos de un diccionario en python 
#Eliminar todo o parte de un diccionario con del 
teclado = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

del teclado1['Precio']
print(teclado)
#Se elimina la clave precio junto con el valor que se habia guardado en este
#Añadir claves adicionales y valores nuevos a un diccionario 
teclado = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado1['Color'] = 'Negro'
print(teclado)
#Ejercicios python 
#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola.
#del nombredediccionario podriamos borrar todo pero si queremos algo especifico como la clave categoria o precio solo es necesario escribirlo asi: del teclado['Categoria']
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2['Modelo'])
