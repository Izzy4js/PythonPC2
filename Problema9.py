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
