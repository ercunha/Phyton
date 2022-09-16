# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# Calcula a média das 3 notas
import sys


def CalculaMedia(n1,n2,n3):
    return (n1+n2+n3) /3

# Valida nota do aluno (Média >= 7 Aprovado SE NÃO Reprovado)
def ValidaNota(media):
    if(media>= 7.0):
        return 'APROVADO'
    else:
        return 'REPROVADO'

op = 'S'
while(op == 'S'):

    nome = input('\n Informe o nome do aluno: ').upper()
    n1 = float(input('Informe a nota 1: '))
    n2 = float(input('Informe a nota 2: '))
    n3= float(input('Informe a nota 3: '))

    media = CalculaMedia(n1,n2,n3)
    print('\n A média aritmética de notas do aluno(a) {0} é de {1} e o aluno está {2}.' .format(nome,media,ValidaNota(media)))
    op = input('\n Deseja continuar ?  (S = SIM | N = NÃO)').upper()
else:
    print("\n Finalizando..." )
    sys.exit()
