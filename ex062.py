# Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra
# quabdo ele disser que quer mostrar 0 termos
primeiro = int(input('Digite o 1° termo de uma P.A: '))
razão = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
dez = 10
total = 0
while dez != 0:
    total = total + dez
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo += razão
        cont += 1
    print('pausa:')
    dez = int(input('Quantos termos a mais você quer ver? '))
print('A Progreção foi finalizada com {} termos.'.format(total))
