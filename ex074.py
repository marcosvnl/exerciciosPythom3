# Crie um programa que vai gerar cinco  números aleatorios e colocar em uma tupla. Depois disso, mostre a listagem
# de números gerados e também indique o menor e o maior que estão na tupla.

from random import randint
sorteio = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print('Números sorteados: ',end=' ')
for c in sorteio:
    print(f'{c}', end=' ')
print(f'\nO maior número : {max(sorteio)}')  # max = Mostra o maior número da tupla
print(f'O menor número: {min(sorteio)}')  # min = Menor número da tupla
