# 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares
# e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

números = [[], []]
num = 0
print(30*'\33[1;32m-=\33[m')
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        números[0].append(num)
    else:
        números[1].append(num)
print(30 * '\33[1;32m-=\33[m')
números[0].sort()
números[1].sort()
print(30 * '\33[1;32m-=\33[m')
print(f'Lista par - {números[0]}')
print(f'Lista impar - {números[1]}')
print(30 * '\33[1;32m-=\33[m')
