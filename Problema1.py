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
