#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

#Imprimindo trinta sinais de igual lado a lado
print('='*30)
#Centralizando a mensagem
print('{:^30}'.format('BEM VINDO(A) AO BANCO E.R'))
print('='*30)

valor = float(input('Qual o valor a ser sacado? '))
ced = 50
total = valor
totCed = 0
op='S'
while(op == 'S'):
    #Enquanto o total for maior que 50 em vou tirando 50 e atualizando o contador
    if(total>=ced):
        total -= ced
        totCed+=1
    else:
        print(f'Total de {totCed} cédulas de R${ced}')
        #Se a cédula atual for a de 50 quer dizer que não consigo tirar mais 50 do valor
        if(ced == 50):
            #Atualizo a cedula para 20
            ced == 20
        elif(ced == 10):
            # Atualizo a cedula para 10
            ced = 10
        elif(ced == 10):
            # Atualizo a cedula para 1
            ced = 1
        totCed=0
        if(total == 0):
           op = 'N'

else:
    # Imprimindo trinta sinais de igual lado a lado
    print('=' * 30)
    # Centralizando a mensagem
    print('{:^30}'.format('ENCERRANDO A OPERAÇÃO. OBRIGADO E VOLTE SEMPRE!'))
    print('=' * 30)




