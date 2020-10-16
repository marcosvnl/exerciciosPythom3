# 032 Faça um programa que Leia um ano qualque e mostre se ele é bissexto.
# para representar sinal de diferente usamos !=
# a biblioteca datetime trabalha com dia e ano atual da maquina
from datetime import date
ano = int(input('Digite um ano para saber se ele é BISSEXTO, digite 0 se quise saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é BISSEXTO'.format(ano))
