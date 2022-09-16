#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
import sys

op = 'S'
while(op =='S'):
    numero = float(input('Informe um número real: '))

    print('\n A fração inteira de {0} é : {1} ' .format(numero,math.trunc(numero)))
    op = input('\n Deseja continuar executando? S = Sim ou N = não: ' ).upper()

else:
    print('Saindo da aplicação ...')
    sys.exit()