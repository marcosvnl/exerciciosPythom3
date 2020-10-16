# 038 Escreva um programa que leia 2 númerosinteiros e compari-os,
# mostrando na tala uma mensagem:
#    - O primeiro é maior q o segundo
#    - O segundo é maior q o primeiro
#    - Não existe valor maior os dois são iguais!
print('\33[1;36m-=\33[m'*20)
print('Coparador de números inteiros')
print('\33[1;36m-=\33[m'*20)
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if  num1 > num2:
    print('O PRIMEIRO é maior do que o segundo!')
elif num2 > num1:
    print('O SEGUNDO é maior que o primeiro!')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais!')
