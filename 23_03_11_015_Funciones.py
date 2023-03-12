#Alan de Jesus Fabian Garcia 11 de marzo de 2023
#Ejemplo capitulo 34
#Creacion de funciones 
def saluda():
	print("Bienvenidos a Programación fácil.")

saluda()
#Argumentos en funciones,son variables especifidas por defecto al llamar a una funcion 
def saluda(nombre, apellidos):
    print('Hola', nombre, apellidos)

saluda('Alan de Jesus ', 'Fabian Garcia')
saluda('Andrea', 'Gomila García')
#Ejercicios python 
#51Crea una función que realice una suma. Para ello, tendrás que añadir dos argumentos (numero1 y numero2). En su interior, especificarás un print() que muestre el resultado de la suma. Deberás hacer tres llamadas que como resultado de la suma den los valores 30, 50 y 57000. Los números que introduzcas en la llamada pueden ser los que quieras siempre que coincidan los resultados en el print().
def suma(numero1, numero2):
    print(numero1+numero2)
    
suma(10,20)
suma(20,30)
suma(50000, 7000)
#Ejemplo capitulo 35
#Argumentos arbitrarios *args
def alumnos(*args):
	print('El primer alumno es ' + args[0] + ' y el último es ' + args[3] + '.')

alumnos('Andrés', 'Ana', 'Andrea', 'Antonio')

#Ejercicios python 
#52.¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')
#Respuesta---------------------------------------
#en la primera linea de colores:son cuatro argumentos. 
#en la linea 2:tres argumentos.
#en la linea 3:un argumento.
#en la linea 4: dos argumentos.

#53Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores()
#Los argumentos en la llamada deben ser dos 
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'azul')
#54Crea una función que realice la suma de cinco números utilizando solo *args. Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().
def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)

suma(9, 12, 50, 8000, 30, 40)
#Capitulo 36----------------------------------------
#**kwargs diccionarios arbitrarios 
def colores (**kwargs):
	print("Este es el color " + kwargs['color1'] + '.')

colores(color1='rojo', color2='azul')
#Cuando queremos utilizar argumentos arbitrarios en diccionarios, *args no nos va a servir, ya que los diccionarios constan de dos subapartados. En este caso, necesitas usar **kwargs.
#No hay ejercicio python 
