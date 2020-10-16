# 033 faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a1 = int(input('Digite um número: '))
a2 = int(input('Digite outro número: '))
a3 = int(input('Mais um número: '))
# Verificando o número menor:
if a1 < a2 and a1 < a3:
    menor = a1
if a2 < a1 and a2 < a3:
    menor = a2
if a3 <a1 and a3 < a2:
    menor = a3
print('O número MENOR é o {}'.format(menor))
# verificando o número menor:
if a1 > a2 and a1 > a3:
    maior = a1
if a2 > a1 and a2 > a3:
    maior = a2
if a3 > a1 and a3 > a2:
    maior = a3
print('O número MAIOR é o {}'.format(maior))
