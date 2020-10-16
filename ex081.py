# Crie um programa que vai ler varios números e colocalos em uma lista.
# Depois mostre:
# A - Quantos números foram digitados
# B - A lista de valores, ordenada de forma decrescente
# C - Se o valor 5 foi digitadoe está ou não na lsita

números = list()
while True:
    números.append(int(input('Didite um valor inteiro: ')))
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Quer adicionar um novo valor inteiro? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
fim = 0
for posição, valor in enumerate(números):
    if números[-1]:
        fim = posição
print(f'Foram digitados {posição + 1} números')
números.sort(reverse=True)
print(números)
if 5 not in números:
    print('O número 5 não foi digitado e não está na lista')
else:
    print('O número 5 foi digitado e está na lista')