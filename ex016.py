# 016 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Ditite o número 6.127 o número 6.127 tem a parte inteira 6.
import math
num = float(input('Digite um número inteiro: '))
# math.trunc = vai te mostar a parte inteira de um número Ex: 6.127 iara mostar o 6
print('A parte inteira de {} é {}'.format(num, math.trunc(num)))
# ou fazer importando apenas o comando trunc "from math import trunc
# nesse caso na resolução do coamndo não precisa colocar math. antes do trunc
# ou fazer apenas com o comando int o mesmo do primitivo q indica um número inteiro
# nesse caso a resolução fica: .format(num, int(num))
