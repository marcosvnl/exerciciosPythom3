# Crie um Ptograma que tenha uma tupla única com nomes de produtos e seus respectivos preçosn na sequência.
# No final, mostre uma listagem de preços organizando os dosdos em forma tabular.
lista = 'Notbook', 5000,\
        'Mouse', 50,\
        'Impresora', 400,\
        'SmartTV', 2500,\
        'Smarphone', 2800
print(40*'=')
print(f'\33[1;32m{"Lista de produtos e preços:":^40}\33[m')
print(40*'=')
for conta in range(0, len(lista)):
    if conta % 2 == 0:
        print(f'{lista[conta]:.<30}', end='')
    else:
        print(f'R$ {lista[conta]:>7.2f}')
