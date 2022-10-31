#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.
import sys

op = 'S'
while op =='S':
    numeros = []
    for i in range (1,10):
        n = int(input(f'Informe um valor: '))
        if n not in numeros:
            numeros.append(n)
        else:
            print('Número informado já se encontra na lista!')


    lista = '='.join(map(str,numeros))
    print(lista)
    numeros.sort()
    ord = '='.join(map(str, numeros))
    print(f'Numéros únicos digitados em ordem crescente: {ord}')
    numeros.sort(reverse=True)
    dec = '='.join(map(str, numeros))
    print(f'Numéros únicos digitados em ordem decrescente: {dec}')

    op = input('Deseja continua? ').upper()[0]
else:
    print('Encerrando...')
    sys.exit()
