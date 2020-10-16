# Programa que leia o comprimento de três retas e diga oq usúario se eles podem ou não formar um triângulo.
l1 = float(input('Digite o comprimento de uma reta; '))
l2 = float(input('Digite o valor de outra reta: '))
l3 = float(input('Digite o valor de outra reta: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com {}, {}, {} é possivel formar um triangulo!'.format(l1, l2, l3))
else:
    print('Com {}, {}, {} não é possival formar um triangulo!'.format(l1, l2, l3))
