#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
número = int(input('Digite um numero de 0 á 9999: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print('O número escolhido pe {}'.format(número))
print('{} unidade'.format(u))
print('{} Dezena'.format(d))
print('{} Centena'.format(c))
print('{} Milhar'.format(m))
