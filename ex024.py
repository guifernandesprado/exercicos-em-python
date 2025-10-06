#Esse programa lê o salário de um funcionário e mostra seu novo salário, com 15% de aumento para salários até R$1250,00 ou 10% para salários acima disso.

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} ,agora passa a ganhar R${:.2f}.'.format(salário,novo))