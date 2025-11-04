#esse programa lê uma frase e diz se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase:')).strip().upper()                #li a frase e tirei os espaços antes e depois
palavras = frase.split()                                               #splitei a frase para gerar uma lista
junto = ''.join(palavras)                                              #juntei as palavras
inverso = ''
for letra in range (len(junto) - 1 , - 1 , -1):
    inverso += junto [letra]                                            #aqui é o inverso da frase digitada
print('O inverso de {} é {} .'.format(junto,inverso))
if inverso == junto :
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')                     #teste para saber se existe o palíndromo