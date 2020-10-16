# Faça um porgrama que leia 5 valores númericos e guarde em uma lista.
# No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posição na lista.
# NOTA: Se o número maior ou menor repetir, mostrar todas as posições
números = []
maior = 0
menor = 0
for c in range(0, 5):
    números.append(int(input(f'Digite o valor na posição {c}:')))
    if c == 0:
        maior = menor = números[c]
    else:
        if números[c] > maior:
            maior = números[c]
        if números[c] < menor:
            menor = números[c]

print(f'\nO MAIOR número foi {maior} na posição:', end=' ')
for lista, valor in enumerate(números):
    if valor == maior:
        print(f'{lista} ', end='')
print(f'\nO MENOR númemo foi {menor} na posição:', end=' ')
for lista, valor in enumerate(números):
    if valor == menor:
        print(f'{lista}', end=' ')
