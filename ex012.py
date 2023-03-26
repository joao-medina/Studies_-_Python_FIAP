#número de refeições
n_refeiçoes = int(input("Informe o número de refeições feitas: "))

calorias = 0  #calorias iniciais
contador = 1  #número ordinal

for c in range(1, n_refeiçoes + 1):
    calorias += int(input("Informe o número de calorias da {}ª refeição: ".format(contador)))
    contador += 1

print("Você consumiu {} calorias.".format(calorias))
