expressão = str(input('Digiete uma expressão: '))
pilha = []
for simbolos in expressão:
    if simbolos == '(':
        pilha.append('(')
    elif simbolos == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta incorreta')
