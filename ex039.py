# 039 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a seua idade:
#   - Se ele ainda vai se alistar ao serviso militar
#   - Se é a hora de se alistar
#   - Se já passou do tempo do alistamento
from datetime import date
print('-='*20)
print('Seviso de alistamento militar brasileiro')
print('-='*20)
ano = int(input('Digite o ano de nascimento: '))
ano1 = date.today().year
if ano1 - ano < 18:
    print('Não esta em faze de ALISTAMENTO MILITAR, fatam {} anos para faze de alistamento!'.format(18-(ano1-ano)))
elif ano1 - ano == 18:
    print('Você esta em ano de ALISTAMENTO MILITAR!')
elif ano1 - ano:
    print('O ALISTAMENTO MILITAR esta atrasado a {} anos,'.format((ano1-ano)-18))
    print('Procure o SERVISO MILETAR em sua região para regularizar sua situação!')
