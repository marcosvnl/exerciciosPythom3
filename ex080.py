# Crie um programa onde o usúario possa digitar cincovalores númericos e cadatrar em uma lista
# , já na posição correta (semusar o sort())
números = []
for lista in range(0, 5):
    n = (int(input(f'Digite um número na posição {lista}: ')))
    if lista == 0 or n > números[-1]:
        números.append(n)
        print('Adicionado ao final da lista')
    else:
        posição = 0
        while posição < len(números):
            if n <= números[posição]:
                números.insert(posição, n)
                print(f'número adicionado na posição {posição}ª')
                break
            posição += 1
print(f'Lista de números {números}')
