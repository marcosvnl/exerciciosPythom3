# crie um programa que leia duas notas de uma luno e colcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida.
print('\33[1;31m-=\33[m'*20)
print('Calculadora de média')
print('\33[1;32m-=\33[m'*20)
p1 = float(input('Digite sua 1° nota: '))
p2 = float(input('Digite sua 2° nota: '))
média = (p1+p2) / 2
if média >= 6:
    print('\33[1;32m;) PARABÉS, sua nota é {:.2f} e esta acima da média !!!\33[m'.format(média))
elif 5 <= média < 5.9:
    print('\33[1;33mRECUPERAÇÃO, sua nota é de {:.2f} e não atingiu a média mínima. Mais tem uam uma chance!\33[m'.format(média))
else:
    print('\33[1;31m=( INFELISMENTE sua nota é {:.2f} e não atingiu a média mínima.\33[m'.format(média))
