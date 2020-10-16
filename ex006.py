# 006 Crie um programa que leia um número e mostre o seu dodro, triplo e raiz quadrada.
n = int(input('Digite um número inteiro: '))
d = n * 2
t = n * 3
q = n ** (1/2)
print('O número qu você escolheu é o: {}'.format(n))
print('O dobro de {} é: {}'.format(n, d))
print('O triplo de {} é: {}'.format(n, t))
print('E sua raiz qualdrada é: {}'.format(q))
