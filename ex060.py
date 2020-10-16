# 060 Faça um programa que leia um número qualquer e mostre o fatorial:
# Ex: 5! = 5*4*3*2*1 = 120
# num = int(input('Digite um um número para saber seu fatorial: '))
# mult = 1
# for c in range(num, 0, -1):
#     mult *= c
#print(mult)
num = int(input('Digite um um número para saber seu fatorial: '))
cont = num
mult = 1
print('Fatorial de {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' X ' if cont > 1 else ' = ', end='')
    mult *= cont
    cont -= 1
print(mult)
