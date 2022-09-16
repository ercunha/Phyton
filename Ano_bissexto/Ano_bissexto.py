#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

op = 'S'
while(op =='S'):
    ano = int(input('Informe o ano: '))
    if ano%4 ==0:
        print('\n O ano de {0} é BISSEXTO: ' .format(ano))
    else:
        print('\n O ano de {0} é NÃO É BISSEXTO: '.format(ano))

    op = input('\n Deseja continuar executando? S = Sim ou N = não: ' ).upper()

else:
    print('Saindo da aplicação ...')
    sys.exit()