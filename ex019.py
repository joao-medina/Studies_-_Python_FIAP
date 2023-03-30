from ex018 import somar, diferenca, multiplicacao

a = int(input("Insira um valor: "))
b = int(input("Insira outro valor: "))

soma = somar(a, b)
dif = diferenca(a, b)
multip = multiplicacao(a, b)



print(f"A soma é de {a} e {b} é igual a {soma}.")
print(f"A diferença entre {a} e {b} é {dif}.")
print(f"A multiplicação entre {a} e {b} é {multip}")