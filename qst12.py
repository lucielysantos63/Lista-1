def encontrar_menor_maior(lista):
    menor = lista[0]
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
        
    return [menor, maior]

numeros = [12, 45, 7, 23, 56, 89, 34]
resultado = encontrar_menor_maior(numeros)

print("Menor número:", resultado[0])
print("Maior número:", resultado[1]) 