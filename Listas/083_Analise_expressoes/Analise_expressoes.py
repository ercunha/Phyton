#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
import sys

op = 'S'
while op == 'S':
    a = 0
    f =  0
    exp = input('Digite uma expressão qualquer que contenha parênteses: ').upper()

    for e in exp:
        if e == '(':
            a+=1
        elif e == ')':
            f+=1

    #Verificando se todos parênteses abertos foram fechados
    if a == f:
        print(f'A espressão {exp} é uma expressão válida!')
    else:
        print(f'A espressão {exp} é uma expressão inválida!')

    op = input('Deseja continuar? ').upper()[0]
else:
    print('Saindo...')
    sys.exit()
