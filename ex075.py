# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
# a) quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.
números = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os valores: {números}')
print(f'O número 9 aparece {números.count(9)} vezes')
print(f'O número 3 apareceu na {números.index(3) +1}° posição primeiro')
print('Os valores pares são: ', end=' ')
for c in números:
    if c % 2 == 0:
        print(c, end=' ')
