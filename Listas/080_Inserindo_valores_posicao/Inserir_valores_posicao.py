#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
import sys

op = 'S'
while op == 'S':
    numeros = []
    for i in range(0,5):
        n = int(input(f'Informe um valor: '))
        #Se for a primeira inserção
        if i == 0 or n > numeros[-1]:
            numeros.append(n)
        else:
            if numeros.__contains__(n):
                print('Número já foi adicionado anteriormente')
            else:
                pos = 0
                while pos < len(numeros):
                    if n <= numeros[pos]:
                        numeros.insert(pos,n)
                        break
                    pos +=1
    lista = '-'.join(map(str, numeros))
    print('='*30)
    print(f'Lista de números ={lista}')
    print('=' * 30)
    op = input('Deseja continuar? ').upper()[0]
else:
    print('Saindo da aplicação...')
    sys.exit()