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
