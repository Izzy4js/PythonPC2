"""
Problema 3:
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

