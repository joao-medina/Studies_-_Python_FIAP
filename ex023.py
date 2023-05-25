tupla = (1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5)
print(f"A tupla foi criada assim: {tupla}")

for c, valor in enumerate(tupla):
    print(f"No indice {c} temos o valor {valor}.")

print(f"Quantidade: {len(tupla)}")

print(f"Máximo: {max(tupla)}")

print(f"Mínimo: {min(tupla)}")

print(f"Soma: {sum(tupla)}")