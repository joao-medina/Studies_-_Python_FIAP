#número de transações
n_transação = int(input("Informe o número de transações realizadas no dia: "))

soma_transação = 0 #valor inicial
contador = 1 #número ordinal

for c in range(1, n_transação + 1):
    soma_transação += float(input("Informe o valor da {}ª transação: ".format(contador)))
    contador += 1

print("O total gasto no dia foi de R${:.2f}".format(soma_transação),
      "\nO valor médio gasto por transação foi de R${:.2f}".format(soma_transação / n_transação))