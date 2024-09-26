"""
Problema 1:
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).
"""

divi = []

for num in range(1499, 2701):
    if num % 5 == 0 and num % 7 == 0:
        divi.append(num)

print("Los números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:", divi)

""" Problema 2:
Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
extrella = int(input("Ingrese un número(1-10):"))

for i in range(1, extrella + 1):
    print("* " * i)

for i in range(extrella - 1, 0, -1):
    print("* " * i)

""" Problema 3:
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
"""

par = 0
impar = 0
lista = [] 
parar = "si"

while parar.lower() == "si":
    while True:
        try:
            numero = int(input("Ingresa un número entero: "))
            break 
        except ValueError:
            print("Error: Por favor ingresa un número entero válido (no decimal).")
    
    
    lista.append(numero)
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

    parar = input("¿Deseas ingresar otro número? (si/no): ")

print(f"Números pares: {par}")
print(f"Números impares: {impar}")
print("Números ingresados:", lista)

"""
Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
"""

alumnos = []

n = int(input("Cuántos alumnos tiene: "))

for i in range(n):
    nombre = input(f"Nombre del alumno {i + 1}: ")
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Calificación {j + 1} de {nombre}: "))
                if 0 <= nota <= 20:  
                    notas.append(nota)
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 20.")
            except ValueError:
                print("Error: Por favor ingrese un número válido para la calificación.")
    
    promedio = sum(notas) / len(notas) if notas else 0
    
    alumnos.append({"Alumno": nombre, "Notas": notas, "Promedio": promedio})

for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}, Promedio: {alumno['Promedio']:.2f}")

""" Problema 5:
Escribe un programa que encuentre la suma de todos los números primos menores que 100.

"""
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


suma = 0
primos = []

for num in range(100):
    if es_primo(num):
        primos.append(num) 
        suma += num  

print("La suma de los numeros primos:", primos, "es:", suma)

""" Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.
"""

def fibo():
    fib_lista = []
    a, b = 0, 1
    
    while a <= 50:
        fib_lista.append(a)
        a, b = b, a + b 
    return fib_lista

serie_fibonacci = fibo()
print("Fibonacci:", serie_fibonacci)

""" Problema 7:
Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
(excluyendo el propio número).
Ejemplo Identificar número perfecto:
Número perfecto: 6
● Divisores propios: 1, 2, 3
● Suma de los divisores propios: 1 + 2 + 3 = 6
"""
def perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:  
            suma += i
    
    return suma == n

numeros = []

for num in range(1, 1000):
    if perfecto(num):
        numeros.append(num)

print("Números perfectos:", numeros)

""" Problema 8:
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.
"""
def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if n == 0 or n == 1:
        return 1 
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


numero = int(input("Ingresa un número: "))
try:
    print(f"El factorial de {numero} es: {factorial(numero)}")
except ValueError as e:
    print(e)

"""Problema 9:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
- Input: Twitter Output: Twttr
- Input: What's your name? Output: Wht's yr nm?
"""
def sin_vocales(texto):
    vocales = "aeiouAEIOU"
    txt_sin_vocales = "".join(caracter for caracter in texto if caracter not in vocales)
    return txt_sin_vocales

palabra = input("Escriba lo que desee: ")

resultado = sin_vocales(palabra)
print("Texto sin vocales:", resultado)

""" Problema 10:
En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
1636!
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
[
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]
Luego, genere esa misma fecha en formato AAAA-MM-DD.
Ejemplos:
- Input: 9/8/1636 | Output: 1636-09-08
- Input: Septiembre 8, 1636 | Output: 1636-09-08
- Input: 1/1/1970 | Output: 1970-01-01
"""

def convertir(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    
    if '/' in fecha:
        mes, dia, año = map(int, fecha.split('/'))
    else:
        parte = fecha.split()
        mes = meses.index(parte[0]) + 1 
        dia = int(parte[1].rstrip(',')) 
        año = int(parte[2]) 

    return f"{año}-{mes:02}-{dia:02}"

fec_input = input("Ingresa una fecha (MM/DD/AAAA o 'Mes día, AAAA'): ")

fec_convertida = convertir(fec_input)
print("Fecha en formato AAAA-MM-DD:", fec_convertida)
