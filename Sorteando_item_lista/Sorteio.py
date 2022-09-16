#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos
# e escrevendo na tela o nome do escolhido.
import random
import sys

op = 'S'
while(op =='S'):
    a1 = input('Informe o nome do aluno 1: ').upper()
    a2 = input('Informe o nome do aluno 2: ').upper()
    a3 = input('Informe o nome do aluno 3: ').upper()
    a4 = input('Informe o nome do aluno 4:').upper()
    lista =  [a1,a2,a3,a4]

    sorteado = random.choice(lista)

    print("Alunos na lista: " ,lista)
    print("Aluno sorteado: " ,sorteado)

    op = input('\n Deseja continuar executando? S = Sim ou N = não: ' ).upper()

else:
    print('Saindo da aplicação ...')
    sys.exit()
