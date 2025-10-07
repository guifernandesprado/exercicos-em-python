#Esse programa lê o valor de uma casa, o salário de uma pessoa e em quantos anos ela vai pagar. Calcula o valor da prestação mensal e diz se o empréstimo será concedido ou não, sabendo que ele não pode ultrapassar 30% do salário.

casa = float(input('\033[4;33;40m Qual o valor da casa? R$'))
salário = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você vai querer pagar?\033[m'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print ('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f} .'.format(casa,anos,prestação))
if prestação <= mínimo :
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado!')