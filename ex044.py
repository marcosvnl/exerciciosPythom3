# 044 Elabore um progrma que calcule o valor a ser pago por um produto, considerando o seu preço normal e condições de pagamento:
#   - á vista / dinheiro: 10% de desconto
#   - á vista no crtão: 5% de desconto
#   - em até 2X preço normal
#   - 3X ou mais nocratão 20% de juros
print('\33[;1;36;40m{:=^40}\33[m'.format(' LOJINHA '))
preço = float(input('Digite o preço do produto: R$'))
fdp = int(input('''Selecione uma forma de pagamento:
[1] - Dinehiro
[2] - Á vista no cartão
[3] - 2X crtão de crédito
[4] - 3X á 12X no crtão de crédito
Opção: '''))
a = preço - preço * 0.10
b = preço - preço * 0.05
d = preço + preço * 0.20
if fdp > 0 and fdp >= 5:
    print('\33[1;31mOpção invelida!\33[m')
elif fdp == 1:
    print('Em dinheiro terá 10% de desconto o novo valor é de R${:.2f}'.format(a))
elif fdp == 2:
    print('Á vista no cartão terá 5% de desconto o novo valor é de R${:.2f}'.format(b))
elif fdp == 4:
    x = int(input('Quantas vezes?: '))
    if 2 < x < 13:
        v = d / x
        print('Em {} vezes de {}, valor com acrescimo de 20% o valor total é de {}'.format(x, v, d))
    else:
        print('\33[1;31mQualtidades de parcelas invalida!\33[m')
else:
    print('Em até 2X no cartão o valor é de {}'.format(preço))
