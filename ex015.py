# Escreva uma programa que pergunte a quantidade de Km
# percorridos por um carro alugado ea quantidae de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
# por dia e R$0,15 por Km rodado
dia = float(input('Quantos dias de locação do veiculo: '))
km = float(input('Quantos KM foram rodados: '))
dias = dia * 60
kms = km * 0.15
total = dias + kms
print('Custo total de locação do veiculo é de: R${}'.format(total))
