#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.
import sys
from math import cosh,tanh,sinh

op = 'S'
while( op =='S'):
    ang = int(input('\n Informe o valor do ângulo: '))

    seno = sinh(ang)
    cos = cosh(ang)
    tang = tanh(ang)
    print('O SENO = {0} e COSENO = {1} e TANGENTE =  {2}. '.format(seno,cos,tang))

    op = input('\n Deseja calcular outro ângulo? ').upper()

# Se não, finaliza o programa
else:
    print("\n Finalizando...")
    sys.exit()