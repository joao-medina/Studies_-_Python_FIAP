valor_bruto = float(input("Informe o valor do pacote: "))
valor_início = valor_bruto
categoria = input("Informe a categoria dos assentos: ").lower()
quantidade_de_viajantes = int(input("Informe a quantidade de viajantes: "))

if categoria == "econômica":
    if quantidade_de_viajantes == 2:
        valor_bruto = valor_bruto * 0.97
    if quantidade_de_viajantes == 3:
        valor_bruto = valor_bruto * 0.96
    if quantidade_de_viajantes >= 4:
        valor_bruto = valor_bruto * 0.95
elif categoria == "executiva":
    if quantidade_de_viajantes == 2:
        valor_bruto = valor_bruto * 0.95
    if quantidade_de_viajantes == 3:
        valor_bruto = valor_bruto * 0.93
    if quantidade_de_viajantes >= 4:
        valor_bruto = valor_bruto * 0.92
elif categoria == "primeira classe":
    if quantidade_de_viajantes == 2:
        valor_bruto = valor_bruto * 0.90
    if quantidade_de_viajantes == 3:
        valor_bruto = valor_bruto * 0.85
    if quantidade_de_viajantes >= 4:
        valor_bruto = valor_bruto * 0.80
else:
    print("Categoria de assentos não identificada.")


if categoria == "primeira classe" or categoria == "executiva" or categoria == "econômica":
    print("\033[1;32mValor Bruto: R${:.2f}".format(valor_início))
    print("Desconto: R${:.2f}".format(valor_início - valor_bruto))
    print("Valor com desconto: R${:.2f}".format(valor_bruto))  #valor com desconto
    print("valor médio por pessoa: R${:.2f}\033[m".format(valor_bruto / quantidade_de_viajantes))