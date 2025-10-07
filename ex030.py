#Esse programa verifica o ano de alistamento militar.

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento : '))
idade = atual - nasc
print('Quem nasceu  em {} tem {} anos em {}. '.format(nasc,idade, atual))
if idade == 18 :
    print('Você tem que se alistar  imediatemente!')
elif idade < 18 :
    saldo = 18 - idade
    print('Faltam {} anos para o alistamento.'.format(saldo))
elif idade > 18 :
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))