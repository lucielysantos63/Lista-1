numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

num = int(input("Digite um número: "))

for i in range(len(numeros)):
    if numeros[i] == num:
        numeros[i] = 0
        print("Número encontrado e modificado para zero.")
        break
else:
    print("Esse número não esta na lista.")