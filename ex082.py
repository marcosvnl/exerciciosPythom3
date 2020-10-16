# Crie um progrma que vai ler vários números e colocar em uma lista. depois disso, crie duas listas extras
# que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das listas geradas.

principal = list()
listapar = list()
listaimpar = list()
while True:
    principal.append(int(input('Digite um número:')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer digitar um novo número? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'Lista Principal - {principal}')
for indice, valor in enumerate(principal):
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
print(f'Lista impar - {listaimpar}')
print(f'Lista par - {listapar}')
