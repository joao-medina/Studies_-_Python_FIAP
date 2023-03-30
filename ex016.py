assinatura = str(input("Insira o tipo de assinatura: \n[ Basic    ] \n[ Silver   ] \n[ Gold     ] \n[ Platinum ] \n")).lower()

while True:
    if assinatura == "basic":
        nivel = 0.3
        break
    elif assinatura == "silver":
        nivel = 0.2
        break
    elif assinatura == "gold":
        nivel = 0.1
        break
    elif assinatura == "platinum":
        nivel = 0.05
        break
    else:
        assinatura = str(input("ERRO! Digite uma assinatura válida: "))

faturamento = int(input("Insira o faturamento anual: "))
bonus = faturamento * nivel

print("O bônus tem um valor de R${:.2f}".format(bonus))