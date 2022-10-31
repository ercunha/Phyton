#Crie uma tupla com os 20 primeiros colocados do brasileirão na ordem de colocação.
#Depois mostre:
#Apenas os 5 primeiros colocados
#Os últimos 4 colocados
#Uma lista com ordem alfabética
#Em que posição na tabela está o time do Internacional

clubes = ('Palmeiras',
         'Internacional',
         'Flamengo',
        'Corinthians',
        'Fluminense',
        'Athlético PR',
        'Atlético MG',
        'São Paulo',
        'América MG',
        'Fortaleza',
        'Botafogo',
        'Santos',
        'Bragantino',
        'Goiás',
        'Coritiba',
        'Ceará',
        'Atlético GO',
        'Cuiabá',
        'Avaí',
        'Juventude')

print('='*30)
print('{:^30}'.format('RANKING DOS 5 PRIMEIROS COLOCADOS'))
print('='*30)

for posicao in range(0,(len(clubes[0:5]))):
    print(f'{posicao+1}º =>{clubes[posicao]}')

print('='*30)
print('{:^30}'.format('REBAIXADOS ATÉ O MOMENTO'))
print('='*30)

for c in  clubes[16:20]:
    print(f'{clubes.index(c)+1}º =>{c}')

print('='*30)
print('{:^30}'.format('CLUBES EM ORDEM ALFABÉTICA'))
print('='*30)
print(sorted(clubes))

print('='*30)
print('{:^30}'.format('COLOCAÇÃO DO INTERNACIONAL NA TABELA'))
print('='*30)
clube = 'Internacional'
print(f'O Internacional está na {clubes.index(clube)+1}º colocação na tabela do Brasileirão 2022.')