# 046 - Fça um preograma que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0 com um pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, 0-1, -1):
    sleep(1)
    print(c)
print('\33[1;34;40mFELIZ ANO NOVO\33[m')