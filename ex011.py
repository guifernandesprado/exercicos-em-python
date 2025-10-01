#Esse programa calcula o ano que a pessoa vai se aposentar

from datetime import datetime
from time import sleep
nome = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
idade = datetime.now().year - nasc
if idade >= 65 :
    print('Você já passou dos 65 anos, você já pode se aposentar.')
else:
    print('Vamos calcular quando você pode se aposentar...')
sleep(1)
diferença = 65-idade
aposentar = diferença + datetime.now().year
print(f'O ano que você vai se aposentar é {aposentar}')

