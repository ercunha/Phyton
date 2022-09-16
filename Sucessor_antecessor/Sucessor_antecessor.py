# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Informe um número qualquer: '))

def ShowNumber(n):
    print('O antecessor de {0} é : {1} e seu sucessor é {2}' .format(n,(n-1),(n+1)))

ShowNumber(n)