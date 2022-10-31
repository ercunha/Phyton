#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
import sys

op = 'S'
while op == 'S':
    pilha = []
    exp = input('Informe uma expressão qualquer usando parênteses: ')

    for e in exp:
        if e == '(':
            pilha.append(e)
        elif e == ')':
            #Verifica se já existe algum parentese adicionado
            if len(pilha) >0:
                #removo o parentese adicionado
                pilha.pop()
            else:
                # se não, eu adiciono um novo fechamento
                pilha.append(e)
                break
    print('=' *30)
    if len(pilha) == 0:
        print(f'A expressão {exp} é uma expressão válida!')
    else:
        print(f'A expressão {exp} é uma expressão inválida!')

    op = input('Deseja contiuar? ').upper()[0]

else:
    print('Saindo...')
    sys.exit()
