#012 Faça um algoritmo que leia a preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Digite o preço do produto: '))
desc = preço * 0.05
desc1 = preço - desc
print('Com o desconto de 5% seu produto saira por {:.2f}R$'.format(desc1))
