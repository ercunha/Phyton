#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos
# pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
import sys

op = 'S'
while op == 'S':
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    count = 0
    for linha in range(0,3):
        for coluna in range(0,3):
           matriz[linha][coluna] = int(input(f'Digite um valor para:[{linha},{coluna}]: '))

    print('-='*30)
    for l in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[l][c]:^5}]',end='')
        print()
    print('-='*30)
    op = str(input('Deseja continuar? ')).upper()
else:
    print('Saindo...')
    sys.exit()



