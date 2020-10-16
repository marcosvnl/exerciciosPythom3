# ESSE PROGRAMA É EXTREMEMENTE IMPORTANTE PARA SE TORNAR UM PROGRAMADOR!!!!!!!! (ESTUDAR SEMPRE)
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuario vai
# continuar. no final mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000
# Qual o nome do produto mais barato
preçototal = preçomenor = produto1000 = contador = 0
maisbarato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Digite o valor do produto: R$ '))
    contador += 1
    preçototal += preço
    if preço > 1000:
        produto1000 += 1
    if contador == 1 or preço < preçomenor:  # quando temos uma das opções (menor ou maior)
        preçomenor = preço
        maisbarato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar a cadastrar produtos [S/N}? ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:=^40}'.format('Fim da sua compra'))
print(f'Sua compra foi finalizada em R${preçototal:.2f}')
print(f'Com {produto1000} produtos acima de R$1000')
print(f'O mais barado  foi {maisbarato} e custou {preçomenor:.2f}')
