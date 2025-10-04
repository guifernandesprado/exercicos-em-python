#Esse programa faz o computador "pensar" em um número entre 0 e 5 e o jogador tenta advinhar qual foi o número escolhido.


from random import randint
from time import sleep
computador = randint (0 , 5) #faz o computador pensar
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta advinhar
print('Processando...')
sleep(2)
if jogador == computador:
    print('Você acertou, Parabéns!')
else:
    print('O número que eu pensei foi {}, você perdeu!'.format(computador))