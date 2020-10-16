# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior eo menor peso.
pmenor = 0
pmaior = 0
for dadospeso in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(dadospeso)))
    if dadospeso == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso
print('O maior peso é {}Kg, e o menor peso é o {}Kg'.format(pmaior, pmenor))
