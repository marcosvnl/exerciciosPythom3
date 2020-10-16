# 036 Escreva um porgrama para aprovar o empréstimo bancario para comprar uma casa.
# O programa vai perguntar "o valorda casa" o "salário" do comprador e em "quantos anos" ele vai pagar.
# Calcule o valor da prestção mensal, sabendo que ela não pode exeder 30% do salário ou o emprestimo será negado.
valor = float(input('Informe o valor do imovel: R$'))
salario = float(input('Informe o seu rendimento mensal: R$'))
anos = int(input('Quantidade de parcelas: R$'))
limite = salario * 0.30
parcela = valor / anos
if parcela < limite:
    print('\33[1;32;40mFinaciamento aprovado!\33[m\n{} parcelas de {:.2f}R$'.format(anos, parcela ))
else:
    print('\33[1;31;43mFinaciamento negado!\33[m')
