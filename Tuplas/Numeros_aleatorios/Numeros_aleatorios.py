#Crie um programa que vai gerar cinco números aleatórios e coloca-los em uma tupla.
#Mostre a listagem de números gerados e também indique o menor e maior valor.

from random import randint

numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('='*30)
print('{:^30}'.format('NÚMEROS GERADOS'))
print('='*30)

print(numeros)

print('='*30)
print('{:^30}'.format('MENOR VALOR'))
print('='*30)
print(min(numeros))

print('='*30)
print('{:^30}'.format('MAIOR VALOR'))
print('='*30)
print(max(numeros))