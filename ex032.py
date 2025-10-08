#esse programa lê o ano de nascimento de um atleta e mostra sua categoria, de acordo com a idade.

from datetime import date
atual = date.today() .year
nasc = int(input('Ano de nascimento do atleta : '))
idade = atual - nasc
if idade <= 9 :
    print('O atleta tem {} anos, sua classificação é MIRIM.'.format(idade))
elif idade <= 14 :
    print('O atleta tem {} anos, sua classificação é INFANTIL.'.format(idade))
elif idade <= 19 :
    print('O atleta tem {} anos, sua classificação é JUNIOR.'.format(idade))
elif idade <= 25 :
    print('O atleta tem {} anos, sua classificação é SÊNIOR.'.format(idade))
elif idade > 25 :
    print('O atleta tem {} anos, sua classificação é MASTER.'.format(idade))