# 029 Escreva um programa que leia a velocidade de uma carro.
# Se le ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,0 por cada KM acima do limite.
import random
kmh = int(random.randint(1, 200))
lim = int(80)
if kmh >= lim:
    print('Você foi multado!')
    print('Você esta a {}Km/h e o limite é de 80Km/k.'.format(kmh, lim))
    print('O valar da multa é de: R${:.2f}'.format(kmh * 7))
else:
    print('Você está á {}Km/h dentro do permitido na via!'.format(kmh))
