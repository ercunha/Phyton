#Exercício Python 69: Crie um programa que leia a idade e o sexo de
# várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:

#Criando um dicionário de Pessoas
import sys



totalPessoas = 0
homens = 0
mulheres = 0
outros = 0
maioresIdade = 0
menoresIdade = 0

def apresentarDados(totalPessoas,homens,mulheres,outros,maioresIdade,menoresIdade):

    print('\n \n **** DADOS OBTIDOS ***')
    print(f'Total de pessoas cadastradas:{totalPessoas}')
    print(f'Total de homens cadastrados:{homens}')
    print(f'Total de mulheres cadastradas:{mulheres}')
    print(f'Total de pessoas de outro gênero cadastrados:{outros}')
    print(f'Maiores de idade:{maioresIdade}')
    print(f'Menores de idade:{menoresIdade}')


op = 'S'
while (op == 'S'):

    idade = 0
    #Garantindo que a idade seja maior que zero
    while (idade == 0):
        idade = int(input('Informe a idade da pessoa: '))
        if(idade>=18):
            maioresIdade+=1
        else:
            menoresIdade+=1
    totalPessoas+=1

    sexo =' '
    #Garantindo que sexo seja informado sendo M ou F ou O
    while (sexo not in 'MFO'):
        sexo = str(input('Informe o sexo da pessoa: M = masculino | F = feminino | O = outro: ')[0].upper())
        if(sexo == 'M'):
            homens+=1
        elif(sexo == 'F'):
            mulheres+=1
        else:
            outros+=1

    op = ' '
    #Garantindo que seja validada resposta de S ou N apenas
    while (op not in 'SN'):
        op = input('\n Deseja continuar? ').upper()[0]
        if(op == 'N'):
            apresentarDados(totalPessoas,homens,mulheres,outros,maioresIdade,menoresIdade)


else:
    sys.exit()
