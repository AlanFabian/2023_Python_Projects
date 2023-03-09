#Alan de Jesus Fabian Garcia 03/03/2023
#Ejemplo
smartphones=['Xiaomi','Iphone','Huawei','Samsung'] #lista de cadena de textos 
print(smartphones)#Imprimir de golper todo el contenido de la lista perteneciente a smartphones 
#las listas pueden contener cualquier tipo de dato 
lista1=['texto',10,55.8,'texto']
#Acceder a elementos individuales de la lista probar solo imprimir Huawei
print(smartphones[2])
#Xiaomi
print(smartphones[0])
#Ejercicios python 
#23De la siguiente lista, ¿qué color está en la posición 3?
# Código Python 
#colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]
colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]
print(colores[3])
#24¿En qué posición se encuentra el color 'rojo'? ¿y el 'rosa'?
#Rojo
print(colores[0])
#rosa
print(colores[7])
#25 Crea una lista que contenga los siguientes valores en las posiciones indicadas.
#"uno" en la posición 4.
#"dos" en la posición 1.
#"tres" en la posición 0.
#"cinco" en la posición 2.
#"cuatro" en la posición 3.
numeros=["tres","dos","cinco","cuatro","uno"]
print(numeros)
#Listas 2
#Ejemplo
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila',
           'negro', 'rosa','blanco', 'naranja']
print(colores[-1])
#Ejercicios de python 
coloresE = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#Utiliza las posiciones negativas para acceder e imprimir algunos de los colores de esta lista. Los colores a los que tienes que acceder son 'naranja', 'amarillo', 'lila', 'blanco' y 'rojo'.
#Naranja
print(coloresE[-1])
#amarillo
print(coloresE[-7])
#lila
print(coloresE[-5])
#blanco
print(coloresE[-2])
#rojo
print(coloresE[-10])
#Listas 3
#Ejemplo
hardware = ["Case", "Motherboard", "HDD", "SSD", "CPU", "Graphics card", "RAM", "Power supply"]
del hardware[0]
print (hardware)
del hardware[6]
print(hardware)
del hardware[-1]
print(hardware)
#De esta lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'. Debes utilizar al menos una vez las posiciones negativas para eliminar un color. Después, imprime la lista para ver los colores que se han eliminado.
coloresE2 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#azul
del coloresE2[1]
#marron
del coloresE2[3]
#rosa
del coloresE2[4]
#negro
del coloresE2[-3]
print(coloresE2)
#Eliminar listas python  con remove 

colores = ['rojo', 'azul', 'verde', 'amarillo']
colores.remove('azul')
print(colores)
#Ejercicios de Python 28
#Elimina de la siguiente lista los elementos 'amarillo' y 'rojo'. Solo puedes eliminarlos utilizando el método remove().
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.remove('amarillo')
colores.remove('rojo')
#Eliminar elementos en listas con metodos pop Listas (5)
colores = ['rojo','azul','verde','amarillo']
colores.pop()#si no se especifica elimina el ultimo elemento de la lista si este no es especificado 
print(colores)
colores = ['rojo','azul','verde','amarillo']
almacena_valor =colores.pop(2)
print('El color eliminado y almacenado es: ', almacena_valor)
#Ejercicios de python 29
#Elimina de la siguiente lista los elementos 'azul' y 'blanco'. Solo puedes eliminarlos utilizando el método pop(). Además, tendrás que guardar esos dos colores en una nueva lista.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
color1 = colores.pop(1)
color2 = colores.pop(7)

colores_guardados = [color1,color2]
print(colores_guardados)
#Insertar elementos con append () Listas 6
colores = ['rojo', 'azul', 'verde', 'amarillo']
colores.append('naranja')#Añade elementos al final de la lista
print(colores)
#Ejercicios python 30
#Añade los colores 'fuxia' y 'celeste' a la lista.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.append('fuxia')
colores.append('celeste')
print(colores)
#Insertar elementos con insert()-listas7 Cap 16
colores = ['rojo', 'azul', 'verde', 'amarillo']
colores.insert(0,'naranja')
print(colores) 
#Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. Deberás hacer esto utilizando posiciones de lista negativas.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.insert(-4,'magenta')
colores.insert(-1,'turquesa')
print(colores)
#ordenar elementos con sort() y sorted() listas 8
colores=['rojo','azul','verde','amarillo']
colores.sort()#acomoda la lista de manera ascendente 
print(colores)
#de manera decendente
colores=['rojo','azul','verde','amarillo']
colores.sort(reverse = True)#ordena de manera descendente(z-a)
print(colores)
colores = ['rojo', 'azul', 'verde', 'amarillo']
print(sorted(colores))
print(colores)
#Ejercicios python 32
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón','lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.sort(reverse=True)
print(colores)
#contar elementos con len()-listas9 Cap18
colores = ['rojo', 'azul', 'verde', 'amarillo']
print(len(colores))#solo cuenta los numeros de la lista 
colores = ['rojo', 'azul', 'verde', 'amarillo']
longitud_colores = len(colores)#Guarda el valor de los elementos de la lista en una variable para su utilizacion 
#No hay ejercicios en este capitulo

