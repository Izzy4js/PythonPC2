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

