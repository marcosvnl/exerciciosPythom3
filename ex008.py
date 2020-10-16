# 008 Escreva um programa que leia um valor em metros e o exiba convertido em centimetro e milimetro.
m = float(input('Digite um valor: '))
c = m * 100
mi = m * 1000
print('O valor é {} m \n Em centimetros: {}cm\n Em milimetros: {}mm'.format(m, c, mi))
