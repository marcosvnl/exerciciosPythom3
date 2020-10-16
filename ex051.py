# 051 - desenvolva um programa que leia o primeiro termo e a razão de uma P.A primeiro termo dessa progressão
# progressão aritimetica
primeiro = int(input('Digiter o 1° termo da P.A: '))
razão = int(input('Digite a Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(c, end=' ')
