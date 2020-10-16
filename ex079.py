# Crie um programa onde o usúario possa digitar vários valores numericos e cadastreos em uma lista. Caso o número
# já exista lá dentro ele não será adicionado. No final, serão exibidos todos os valores ínicos digitados em
# ordem crescente.
números = list()
while True:
    num = int(input('Digite um número: '))
    if num not in números:
        números.append(num)
    else:
        print('Valor existente, não sera adicioinado')

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar a cadastra números [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
números.sort()
print(f'{números}')
