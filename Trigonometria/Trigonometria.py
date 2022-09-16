# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import sys
from math import hypot

op = 'S'
while( op =='S'):
    catAdj = float(input('\n Informe o valor do cateto adjacente: '))
    catOpo = float(input('Informe o valor do cateto oposto: '))

    comprimento = hypot(catAdj,catOpo)
    print('O comprimento da hipotenusa com CA = {0} e CO = {1} equivale a {2}. '.format(catAdj,catOpo,comprimento))

    op = input('\n Deseja calcular a hipotenusa de outro triângulo ? ').upper()

# Se não, finaliza o programa
else:
    print("\n Finalizando...")
    sys.exit()
