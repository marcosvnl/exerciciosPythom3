# Desenvolva um logíca que leia o peso e a altura de uma pessoa< calcule seu IMC e mostre seu statos:
#   - Abaixo de 18,5: Abaixo do peso
#   - Entre 18,5 há 25: Peso ideal
#   - de 25 há 30: Sobre-peso
#   - de 30 há 40: Obesidade
#   - Acima de 40: Obesidade mórbida
peso = float(input('Digiete o peso: \33[1;36mKg\33[m'))
alt = float(input('Digite a altura: \33[1;36m(m)\33[m'))
imc = peso / alt**2
if imc <= 18.5:
    print('IMC = \33[1;31;40m{:.3f}\33[m - Esta a baixo do peso ideal'.format(imc))
elif imc > 18.51 and imc < 25:
    print('IMC = \33[1;32m{:.3f}\33[m - Esta no peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC = \33[1;33m{:.3f}\33[m - Esta com sobre peso'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC = \33[1;31m{:.3f}\33[m - Obesidade'.format(imc))
elif imc > 40:
    print('IMC = \33[1;31;43m{:.3f}\33[m - Obesidade mórbida'.format(imc))
