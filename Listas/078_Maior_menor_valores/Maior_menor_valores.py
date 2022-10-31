#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
import sys

op = 'S'
while op == 'S':
    numeros = []
    for i in range(1,5):
        n = int(input(f'Informe um valor para n{i}: '))
        numeros.append(n)

    maiorValor = max(numeros)
    menorValor = min(numeros)
    posicaoMaior = numeros.index(maiorValor)
    posicaoMenor = numeros.index(menorValor)

    print(f'VALORES DA LISTA:{numeros} ')
    print(f'O maior valor encontrado foi de {maiorValor} na posição {posicaoMaior} da lista.')
    print(f'O menor valor encontrado foi de {menorValor} na posição {posicaoMenor} da lista.')

    op = input('Deseja continuar? ').upper()[0]
else:
    print('Saindo da aplicação...')
    sys.exit()
