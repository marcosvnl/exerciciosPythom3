# 017 Faça um porgrama que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
# calcule o comprimento da hipotenusa.
import math
co = float(input('Digite o valor do cateto oposto de uma triângulo retângulo: '))
ca = float(input('Digite o valor do cateto adjacente de um triangulo retângulo: '))
hip = math.sqrt(pow(co, 2) + pow(ca, 2))
# ou apenas utilizando o comando da bibliotéca math.hypot(co, ca)
print('O valor da Hipotenusa é {:.4f}'.format(math.sqrt(pow(hip, 2))))
