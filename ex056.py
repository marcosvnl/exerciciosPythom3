# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# no final dp programamotre:
# - Qual é o nome do homem mais velho
# - A media de idade do grupo
# - Quntas mulheres têm menos de 20 anos
from datetime import date
alt = date.today().year
velhoman = 0
nomeman = ''
contwom = 0
soma = 0
for dados in range(1, 5):
    print('{}° Pessoa'.format(dados))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    soma += idade
    if sexo in 'Ff' and idade < 20:
        contwom += 1
    if dados == 1 and sexo == 'Mm':
        velhoman = idade
        nomeman = nome
    else:
        if idade > velhoman:
            velhoman = idade
            nomeman = nome
media = soma / 4
print('A média entre o grupo de pessoas é de {} anos'.format(media))
print('O Homem mais velho tem {} anos e seu nome é {}'.format(velhoman, nomeman))
print('A {} mulheres com menos de 20 anos no grupo de pessoas'.format(contwom))
