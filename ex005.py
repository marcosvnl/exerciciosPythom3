# 005 faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número qualquer: '))
s = n - 1
a = n + 1
print('Você escolheu o número: {}'.format(n))
print('Seu sucessor é o número: {}'.format(a))
print('E seu antecessor é o número: {}'.format(s))
