# 024: Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome de uma Cidade: ')).strip()
print(cidade[:5].lower() == 'santo')
# dessa forma vc certa um possivel erro de digitação do usuario
# no caso de colocar letras maiusculas e minuscas aleatorias na fase ou na palavra
# vc usando .upper ou .lower vc faz com q o prog jogue tudo de maneira uniforme assim evita esse tipo de problema
# e o .strip parta q ele ignore os espaços no começo e no final da str

