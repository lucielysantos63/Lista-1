numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print("Numeros pares:", numeros_pares)