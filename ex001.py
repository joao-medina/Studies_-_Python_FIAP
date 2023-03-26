valor_compra = float(input("Digite o valor da compra: "))
cupom = input("Digite o cupom de desconto: ").upper()

if cupom == "NIVER10":
    valor_compra = valor_compra * 0.9
else:
    print("Cupom inválido")

print("O valor da compra foi de {}".format(valor_compra))