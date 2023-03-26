valor = int(input("Digite um valor númerico inteiro: "))
i = 0 #contador
primeiro = 0 #primeiro valor a ser somado
segundo = 1 #segundo valor a ser somado

#sequência de Fibonacci
while i <= valor:
    i = primeiro + segundo
    primeiro = segundo
    segundo = i

if valor == primeiro:
    print("Ação bem sucedida!")
else:
    print("A ação falhou...")
