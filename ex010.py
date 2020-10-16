# 010 Crie um programa que leia quanto de dinehiro uma pesoa tem na
# carteira e mostre quantos dólares ela pode comprar.
# Considerar >>> US$1,00=R$3,27
# para limitar quantidades de digitos depois de , > {:.2f} onde 2 é a quantidade de digitos e f de flout
n = float(input('valor em sua carteira de investimento: '))
d = n / 3.27
print('com o valor {:.2f} é possível comprar {:.2f} dolares'.format(n, d))
