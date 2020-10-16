# Crie um progrma que faça p computador jogar Jokempô com você
from random import randint
from time import sleep

print('\33[1;32m-=\33[m' * 10)
print('\33[1;34m!!!JOKEMPÔ!!!\33[m')
print('\33[1;32m-=\33[m' * 10)
lista = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Faça sua escolha:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
usuario = (int(input('Sua escolha: ')))
print('O computador escolheu {}'.format(lista[computador]))
print('Você esconheu {}'.format(lista[usuario]))
print('JO !!!')
sleep(1)
print('KEN !!!')
sleep(1)
print('PO !!!')
if computador == 0:  # PC escolhe PEDRA
    if usuario == 0:
        print('EMPATAMOS')
    elif usuario == 1:
        print('Você ganhou PARABÉS!')
    elif usuario == 2:
        print('COMPUTADOR VENCE ;)')
    else:
        print('Opção invalida')
elif computador == 1:  # PC escolhe PAPEL
    if usuario == 1:
        print('EMPATAMOS')
    elif usuario == 2:
        print('Você ganhou PARABÉS!')
    elif usuario == 0:
        print('COMPUTADOR VENCE ;)')
    else:
        print('Opção invalida')
elif computador == 2:  # PC escolhe TESOURA
    if usuario == 2:
        print('EMPATAMOS')
    elif usuario == 0:
        print('Você ganhou PARABÉS!')
    elif usuario == 1:
        print('COMPUTADOR VENCE ;)')
    else:
        print('Opção invalida')
