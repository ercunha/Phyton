# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
import sys


def Calcula(vl,alt,perc):
    if(alt == 'A'):
        return (vl) + (vl*(perc/100))
    if(alt == 'R'):
        return (vl) - (vl*(perc/100))
    else:
        return 'Você informou uma opção inválida.'

def ValidaAlteracao(alt):
    if(alt == 'A'):
        return 'AUMENTO'
    if(alt == 'R'):
        return 'REDUÇÃO'
    else:
        return 'TIPO DE ALTERAÇÃO NÃO ENCONTRADA'

op = 'S'
while(op =='S'):
    alt = input('Informe [A - Aumentar o valor] ou [R - Reduzir]: ').upper()

    while alt == 'A' or alt == 'R':
        nome = input('\n Informe o nome do produto: ').upper()
        valor = float(input('Informe o valor atual do produto: '))
        perc = float(input('\n Qual o % a ser considerado? '))
        novoValor = Calcula(valor, alt, perc)
        tipoAlteracao = ValidaAlteracao(alt)

        print('Valor atual do produto {0} = R$ {1} '.format(nome, valor))
        print('Novo Valor do produto {0} com {1} de {2}% = R$ {3} '.format(nome, tipoAlteracao, perc, novoValor))

        op = input('\n Deseja continuar calculando o valor para outro produto ? ').upper()
        alt = input('Informe [A - Aumentar o valor] ou [R - Reduzir]: ').upper()
    else:
        alt = input('Informe [A - Aumentar o valor] ou [R - Reduzir]: ').upper()

else:
    print('Saindo da aplicação...')
    sys.exit()
