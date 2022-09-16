#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
import sys

op = 'S'
while(op == 'S'):
    nome = input('Informe o nome completo da pessoa: ').upper().strip()
    if 'SILVA' in nome:
        print('O nome {} tem SILVA nele. ' .format(nome))
    else:
        print('O nome {} NÃO tem SILVA nele. '.format(nome))

    op = input('\n Deseja informar outra cidade?  ').upper()
else:
    print('Saindo...')
    sys.exit()