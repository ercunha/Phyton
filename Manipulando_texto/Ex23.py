#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
import sys

op = 'S'
while(op == 'S'):
    numero = int(input('Informe um número de 0 a 9999: '))
    n = str(numero)
    if numero > 9999:
        numero = int(input('Informe um número de 0 a 9999: '))
        n = str(numero)
    else:
     print('-'.join(n))
     op = input('Deseja continuar? ').upper()
else:
    print('Saindo...')
    sys.exit()

