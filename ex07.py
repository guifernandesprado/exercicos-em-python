#Esse programa calcula a raiz quadrada de um número.

import math
num = int(input('Escolha um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual á {:.2f}.'.format(num,raiz))