idade = int(input("Informe a sua idade: "))
BPM = int(input("Informe o seu batimento cardiaco com minuto (BPM): "))

if idade <= 2:
    if BPM >= 120 and BPM <= 140:
        print("Seu batimento cardíaco está adequado.")
    elif BPM < 120:
        print("Seu batimento cardíaco está a baixo da faixa adequada.")
    else:
        print("Seu batimento cardíaco está a cima do adequado.")

elif idade >= 8 and idade <= 17:
    if BPM >= 80 and BPM <= 100:
        print("Seu batimento cardíaco está adequado.")
    elif BPM < 80:
        print("Seu batimento cardíaco está a baixo da faixa adequada.")
    else:
        print("Seu batimento cardíaco está a cima do adequado.")

elif idade >= 18 and idade <=65:
    if BPM >= 70 and BPM <= 80:
        print("Seu batimento cardíaco está adequado.")
    elif BPM < 70:
        print("Seu batimento cardíaco está a baixo da faixa adequada.")
    else:
        print("Seu batimento cardíaco está a cima do adequado.")

elif idade > 65:
    if BPM >= 50 and BPM<= 60:
        print("Seu batimento cardíaco está adequado.")
    elif BPM < 50:
        print("Seu batimento cardíaco está a baixo da faixa adequada.")
    else:
        print("Seu batimento cardíaco está a cima do adequado.")