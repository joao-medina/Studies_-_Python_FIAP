peso = float(input("Informe o seu peso em quilos: "))
altura = float(input("Informe a sua altura em metros: "))

IMC = peso / (altura * altura)

if IMC < 16.00:
    Categoria = "Baixo peso Grau 3"
elif IMC >= 16.00 and IMC < 17.00:
    Categoria = "Baixo peso Grau 2"
elif IMC >= 17.00 and IMC < 18.50:
    Categoria = "Baixo peso Grau 1"
elif IMC >= 18.50 and IMC < 25.00:
    Categoria = "Peso ideal"
elif IMC >= 25.00 and IMC < 30.00:
    Categoria = "Sobrepeso"
elif IMC >= 30.00 and IMC < 35.00:
    Categoria = "Obesidade Grau 1"
elif IMC >= 35.00 and IMC < 40.00:
    Categoria = "Obesidade Grau 2"
else:
    Categoria = "Obesidade Grau 3"

print("Você possui o IMC de {:.2f}, você está com {}.".format(IMC, Categoria))