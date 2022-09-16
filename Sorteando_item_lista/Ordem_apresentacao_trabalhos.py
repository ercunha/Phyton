#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos
# quatro alunos e mostre a ordem sorteada.
import random
from random import shuffle
import sys

op = 'S'
while(op =='S'):
    a1 = input('Informe o nome do aluno 1: ').upper()
    a2 = input('Informe o nome do aluno 2: ').upper()
    a3 = input('Informe o nome do aluno 3: ').upper()
    a4 = input('Informe o nome do aluno 4:').upper()
    lista =  [a1,a2,a3,a4]
    ordem = random.shuffle(lista)

    print("Ordem dos trabalhos " ,lista)

    op = input('\n Deseja continuar executando? S = Sim ou N = não: ' ).upper()

else:
    print('Saindo da aplicação ...')
    sys.exit()
