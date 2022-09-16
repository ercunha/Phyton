#Exercício Python 28: Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.
import random
import sys

op = 'S'

while(op == 'S'):
    numero = int(input('Informe um número entre 0 - 15: '))
    if numero >15 or numero<0:
        numero = int(input('Informe um número entre 0 - 15: '))
    else:
        pc = random.randint(0,15)
        if numero == pc:
            print('PARABÉNS ! Você acertou.')
            print('Seu número foi: {}' .format(numero))
            print('Número do PC: {}' .format(pc))
        else:
            print('ERROU! Não foi desta vez .')
            print('Seu número foi: {}' .format(numero))
            print('Número do PC: {}' .format(pc))

    op = input('\n Deseja continuar jogando ?').upper()
else:
    print('Saindo da aplicação...')
    sys.exit()