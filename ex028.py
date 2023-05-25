dicionario = {
    "Yoda":"Mestre Jedi",
    "Mace Windu":"Mestre Jedi",
    "Anakin Skywalker":"Cavaleiro Jedi",
    "R2-D2":"Droide",
    "Dex":"Balconista"
    #personagem : categoria
}

dicionario.pop("Yoda")

dicionario.popitem() #remove o último item

for c, n in dicionario.items():
    print(f"{c} -- {n}")