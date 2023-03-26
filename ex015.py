opção = 1
ficha = []
ranking = 1 #para rankear

while opção == 1 or opção >= 3:
    print("\n1 - Inserir restaurante\n"
          "2 - Finalizar\n")
    opção = int(input("Escolha uma opção: "))

    if opção == 1:
        nome = str(input("Insira o nome do restaurante: "))
        nota = float(input("Insira a avaliação deste restaurante: "))
        distância = float(input("Insira a distância em Km deste restaurante: ")) * -1
        #distância * -1 para ordenar de forma crescente
        ficha.append([nota, distância, nome])

    if opção >= 3:
        print("\nOpção invalida. Tente novamente")

ficha.sort()
ficha.reverse()
for c in ficha:
    print("{}° - {}, avaliação {}, distância {}Km".format(ranking, c[2], c[0], c[1] * -1))
    ranking += 1
