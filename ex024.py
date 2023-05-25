lista = [True, False]
tupla = tuple(lista)
print(lista)
print(tupla)

tupla2 = (0, 1)

print(f"Verificando se a todosos valores são verdadeiros: {all(tupla)}")

print(f"Verificando se algum valor é verdadeiro: {any(tupla2)}")