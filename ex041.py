# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de uma atleta e mostre
# sua categori de acordo com sua idade:
# Até 9 anos: Mirin
# Até 14 anos: Infantil
# Até 19 anos: Junior
# até 25 anos: Sénior
# Acima: Mster
from datetime import date
atl = date.today().year
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = atl - ano
print('O Atleta tem {} e é compativel coma categoria:'.format(idade))
if idade <= 9:
    print('\33[;33m     - Mirim\33[m')
elif 9 < idade <= 14:
    print('\33[;34m     - Infantil\33[m')
elif 14 < idade <= 19:
    print('\33[;35m     - Junior\33[m')
elif 19 < idade <= 25:
    print('\33[;34m     - Sénior\33[m')
else:
    print('     - master')
