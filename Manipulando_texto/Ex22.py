#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
import sys

op = 'S'
while(op == 'S'):
    nome = input('Informe o nome completo de uma pessoa: ').title()
    print('Nome com todas letras minúsculas, ', nome.lower())
    print('Nome com todas letras maiúsculas, ', nome.upper())

    #Remove espaços em branco e junta tudo
    nomeAlt = nome.replace(' ','')
    print('o nome {} tem {} caracteres sem considerar espaços: '.format(nomeAlt, len(nomeAlt)))

    # strip() para tirar os espaços antes e depois de cada elemento,
    # split(' ') para separar os elementos delimitando-os por um espaço,
    # [0] para pegar o primeiro elemento do resultado do split()
    primeiroNome = nome.strip().split()[0]
    print('O primeiro nome informado [{}] tem {} caracteres. ' .format(primeiroNome, len(primeiroNome)))
    op = input('\n Deseja continuar? ').upper()

else:
    print('Saindo...')
    sys.exit()

