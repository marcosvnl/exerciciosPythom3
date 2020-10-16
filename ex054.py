# Crie um programa que leia a ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores. maioridade => 21 anos
from datetime import date
tmaior = 0
tmenor = 0
atl = date.today().year
for cont in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(cont)))
    idade = atl - ano
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('{} atingiram a maior idade.'.format(tmaior))
print('{} pessoal não agintiram a maior idade.'.format(tmenor))
