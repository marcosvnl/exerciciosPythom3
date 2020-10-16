# 018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tagente
# desse ângulo.
import math
ângulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ângulo))
print('O valor do SENO de {} é {:.2f}!'.format(ângulo, seno))
coseno = math.cos(math.radians(ângulo))
print('O valor do COSENO de {} é {:.2f}!'.format(ângulo, coseno))
tangente = math.tan(math.radians(ângulo))
print('O valor da TANGENTE de {} é {:.2f}!'.format(ângulo, tangente))
# o comando maht.radians converte o valor para radianos
