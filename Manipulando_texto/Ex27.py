#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
import sys

op = 'S'
while(op == 'S'):
    n = input('O nome completo da pessoa: ').upper().strip()
    nome = n.split()
    primeiro = nome[0]
    ultimo = nome[len(nome)-1]

    print('Primeiro nome = {} e último nome = {} '.format(primeiro,ultimo))

    op = input('\n Deseja informar outra cidade?  ').upper()
else:
    print('Saindo...')
    sys.exit()