"""
Problema 2:
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
