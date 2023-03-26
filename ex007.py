tipo_de_assinatura = input("Tipo de assinatura: ").lower()
faturamento_anual = float(input("Faturamento anual: "))
bonus = 0.0

if tipo_de_assinatura == "basic":
    bonus = 0.3
elif tipo_de_assinatura == "silver":
    bonus = 0.2
elif tipo_de_assinatura == "gold":
    bonus = 0.1
elif tipo_de_assinatura == "platinum":
    bonus = 0.05
else:
    print("Tipo de assinatura não identificada")

print("O valor do bônus é de R${:.2f}".format(bonus * faturamento_anual))