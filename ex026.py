dicionario = {
    "Yoda":"Mestre Jedi",
    "Mace Windu":"Mestre Jedi",
    "Anakin Skywalker":"Cavaleiro Jedi",
    "R2-D2":"Droide",
    "Dex":"Balconista"
    #personagem : categoria
}

print(dicionario.keys())

print(dicionario.values())

print(dicionario.items())

for c, v in dicionario.items():
    print(f"{c} -- {v}")