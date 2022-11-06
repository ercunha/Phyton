#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
import sys

op = 'S'
while op =='S':
    pessoas = list()
    dados_pessoas = list()


    for i in range(1,6):
        n = str(input(f'Informe o nome de p{i}: ')).upper()
        p = int(input(f'Informe o peso de p{i}: '))
        #Adiciona o item a lista com caracteris de nome e peso
        pessoas.append(n)
        pessoas.append(p)
        #Cria uma cópia da lista atualizada de pessoas
        dados_pessoas.append(pessoas[:])
        #Excluir itens da lista de pessoas para que seja adicionado um único item da próxima leitura do laço
        pessoas.clear()


    total_pessoas = len(dados_pessoas)
    mais_pesado = list()
    menos_pesado = list()
    maior_peso = 0
    menor_peso = 0

    #procurando o mais pesado e o menos pesado
    for p in dados_pessoas:
        if p[1] > maior_peso:
            maior_peso = p[1]
            mais_pesado.clear()
            mais_pesado.append(p)
        #Se for a primeira ocorrência do menor peso adiciono
        if  len(menos_pesado) == 0:
            menor_peso = p[1]
            menos_pesado.clear()
            menos_pesado.append(p)
        else:
            if p[1] < menor_peso:
                menor_peso = p[1]
                menos_pesado.clear()
                menos_pesado.append(p)

    print('='*30)
    print(f'Total de pessoas cadastradas:{total_pessoas} pessoas')
    print(f'Pessoas Cadastradas:{dados_pessoas}')
    print(f'Mais pesado:{mais_pesado}')
    print(f'Menos pesado:{menos_pesado}')

    op = input('Deseja continuar? ').upper()[0]
else:
    print('Saindo...')
    sys.exit()

