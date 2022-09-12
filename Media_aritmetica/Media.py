# Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.
import sys


def Calcula(n1,n2,n3):
    return (n1+n2+n3)/3

def ValidaMedia(media):
    if(media >= 7):
        return 'APROVADO'
    else:
        return 'REPROVADO'

op = 'S'
while(op =='S'):

   nome =  input('\n Informe o nome do aluno: ')
   n1 = float(input('Informe o valor de N1: '))
   n2 = float(input('Informe o valor de N2: '))
   n3 = float(input('Informe o valor de N3: '))

   media = Calcula(n1,n2,n3)

   print('O aluno {0} obteve média = {1} e está {2} para o próximo semestre.' .format(nome,media,ValidaMedia(media)))

   op = input("\n Deseja continuar calculando outro valor? [S = Sim ou N = não] ").upper()
else:
    print('Saindo da aplicação...')
    sys.exit()