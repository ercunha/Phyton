#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
import sys

op = 'S'
while(op =='S'):
    n = int(input('Informe o número: '))
    if n%2 == 0:
        print('O número {} é PAR.' .format(n))
    else:
        print('O número {} é ÍMPAR.' .format(n))

    op = input('\n Deseja continuar ? ').upper()
else:
    print('Saindo...')
    sys.exit()