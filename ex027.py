dicionario = dict()

nome = "Frodo"
especie = "Hobbit"

print("Digite 0 para encerrar: ")
while True:
    nome = input("Digite o nome de um personagem:\n")
    if nome == "0":
        break

    especie = input("Digite sua espécie:\n")
    if especie == "0":
        break

    dicionario[nome] = especie



for n, e in dicionario.items():
    print(f"O {n} é um {e}")