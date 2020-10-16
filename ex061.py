# 061 - refaça o "desafio 051", lendo o primeiro termo de uma de uma razão de uma P.A, mostrando os 10 preimeiro
# termos da progressão usando a estrutura while.
primeiro = int(input('Digiter o 1° termo da P.A: '))
razão = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end='-')
    termo += razão
    cont += 1
print('Fim')
