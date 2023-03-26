import math

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

print("{}x^2 + {}x + {}".format(a, b, c))
delta = b**2 - 4 * a * c

if delta == 0:                       #um valor
    valor1 = (-b + math.sqrt(delta )) / (2 * a)
    print("Valor obtido: {}".format(valor1))
elif delta > 0:                     #dois valores
    valor1 = (-b + math.sqrt(delta )) / (2 * a)
    valor2 = (-b - math.sqrt(delta )) / (2 * a)
    print("valores obtidos: {} e {}".format(valor1, valor2))
else:                               #nenhum valor
    print("nenhum valor foi obtido ")