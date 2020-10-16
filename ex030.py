# 030 Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Ímpar.
num = int(input('Digite um número para saber se ele é PAR ou IMPAR: '))
res = num % 2
if res == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))
