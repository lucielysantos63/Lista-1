numeros = [12, 45, 7, 23, 56, 89, 34]
maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print("Maior número:", maior)
print("Menor número:", menor)