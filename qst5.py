frutas = ['uva','banana','abacaxi','laranja','limão']

nome_de_fruta = input("Digite o nome de uma fruta: ")

if nome_de_fruta in frutas:
    print(f"A fruta {nome_de_fruta} está na lista")
else:
    print(f"A fruta {nome_de_fruta} NÃO está na lista")