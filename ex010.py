minuto = int(input("Digite o minuto atual: "))
fatorial = minuto

while minuto != 0:
    minuto -= 1
    if minuto != 0:
      fatorial *= minuto

print("A senha necessária para desbloqueio é LIBERDADE{}".format(fatorial))