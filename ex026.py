# 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição
# ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Escreva uma faze: ')).strip()
minus = frase.lower()
print('Sua frase tem {} letras A!'.format(minus.count('a')))
print('A letra A apareceu em {}° posição na primeira vez'.format(minus.find('a')+1))
print('A letra A aparece em {}° posição na útima vez'.format(minus.rfind('a')+1))
