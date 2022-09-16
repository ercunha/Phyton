#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se
# ela começa ou não com o nome “SANTO”.
import sys

op = 'S'
while(op == 'S'):
    cidade = input('Informe o nome de uma cidade: ').upper()
    c = cidade.strip().split()[0]
    if c == 'SANTO':
        print('A cidade {} começa com o nome SANTO.' .format(cidade))
    else:
        print('A cidade {} não começa com o nome SANTO. '.format(cidade))

    op = input('\n Deseja informar outra cidade?  ').upper()
else:
    print('Saindo...')
    sys.exit()