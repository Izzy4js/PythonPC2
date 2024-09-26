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
