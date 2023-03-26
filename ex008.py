segunda = int(input("Número de votos da segunda-feira: "))
terça = int(input("Número de votos da terça-feira: "))
quarta = int(input("Número de votos da quarta-feira: "))
quinta =  int(input("Número de votos da quinta-feira: "))
sexta = int(input("Número de votos da sexta-feira: "))

#caso segunda tenha mais votos
if segunda > terça and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia mais votado foi segunda-feira.")
#caso terça tenha mais votos
elif terça > segunda and terça > quarta and terça > quinta and terça > sexta:
    print("O dia mais votado foi terça-feira.")
#caso quarta tenha mais votos
elif quarta > segunda and quarta > terça and quarta > quinta and quarta > sexta:
    print("O dia mais votado foi quarta-feira.")
#caso quinta tenha mais votos
elif quinta > segunda and quinta > terça and quinta > quarta and quinta > sexta:
    print("O dia mais votado foi quinta-feira")
#caso sexta tenha mais votos
elif sexta > segunda and sexta > terça and sexta > quarta and sexta > quinta:
    print("O dia mais votado foi sexta-feira.")
#caso haja empate
else:
    print("Houve empate")