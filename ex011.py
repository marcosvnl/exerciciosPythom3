# 011 Faça um programa que leia a largura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-lá
# sabendo que cada litro de tinta, pinta uma área de 2m².
h = float(input('Digite a altura da parede: '))
b = float(input('Digite a largura da parede: '))
a = b * h
tinta = a / 2
print('A area da parede é de: {:.2f}m²'.format(a))
print('Você vai precisar de {}L de tinta!'.format(tinta))

