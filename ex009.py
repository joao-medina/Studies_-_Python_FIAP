impar_soma = 0

for c in range(1,50,2):
    impar_individual = int(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES \n"
                "POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}:  ".format(c)))
    impar_soma += impar_individual

par_soma = 0

for c in range(2,51,2):
    par_individual = int(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES \n"
                "POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}:  ".format(c)))
    par_soma += par_individual

print("A média dos números ímpares é de {:.2f}".format(impar_soma / 25))
print("A média dos números pares é de {:.2f}".format(par_soma / 25))