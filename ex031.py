# 031 Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
dis = float(input('Digite o Km da viagem: '))
print('Sua viagem é de {}Km'.format(dis))
if dis >= 200:
    print('O valor da viagem será de R${:.2f}'.format(dis * 0.45))
else:
    print('O valor da viagem será de R${:.2f}'.format(dis * 0.50))
