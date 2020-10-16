# 028 Escreva uma progra que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário ternta descobrir qual número escolhido pelo computador.
# Oprograma deverá escrever na tela se o usuário venceu ou perdeu.
import random
num = random.randint(0, 5)
print('Escreva um número de 0 á 5, se você acertar o número que o computador pensou ganha')
esc = int(input('Digite um número: '))
print('O computador Escolheu o número {}!'.format(num))
if num == esc:
    print('PARABÉS você venceu!!!')
else:
    print('Você foi DERROTADO!!!')
