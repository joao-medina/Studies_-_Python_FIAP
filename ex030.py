arquivo = open("caminho", encoding="UTF-8")

#print(arquivo.readline()) # lê uma linha
#print(arquivo.read()) # lê o arquivo todo
#print(arquivo.readlines()) # transforma as linhas em uma lista

versos = arquivo.readlines()

for c in versos:
    print(c)

arquivo.close() #fechar arquivo