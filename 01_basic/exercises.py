###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
mi_nombre = "Juan Pérez"
mi_ciudad = "Madrid"

print(f"Mi nombre es {mi_nombre}")
print(f"Vivo en {mi_ciudad}")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"El tipo de dato de a es: {type(a)}")
print(f"El tipo de dato de b es: {type(b)}")
print(f"El tipo de dato de c es: {type(c)}")
print(f"El tipo de dato de d es: {type(d)}")
print(f"El tipo de dato de e es: {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
entero = int(cadena)
flotante = float(cadena)

print(f"El entero es: {entero}")
print(f"El flotante es: {flotante}")

entero_from_float = int(3.99)
print(f"El entero convertido de 3.99 es: {entero_from_float}")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = "Jasir Carvajal"
age = 25
height = 1.83

print(f"Hola me llamo {name} y tengo {age} años, mido {height} metros.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
import math

pi = math.pi
print(f"El valor de PI es: {pi}")
pi_redondeado = round(pi)
print(f"El valor de PI redondeado es: {pi_redondeado}")

numero_division_entera = pi_redondeado // 2
print(f"El resultado de la división entera es: {numero_division_entera}")