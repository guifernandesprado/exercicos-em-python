#esse programa lê o ano de nascimento de sete pessoas e diz quantas são maiores e quantas são menores de idade.

from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range (1 ,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21 :
        tmaior += 1
    else:
        tmenor += 1
print('No total, tivemos {} pessoas maiores de idade e {} pessoas menores de idade.'.format(tmaior,tmenor))