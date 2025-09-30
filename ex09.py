#Esse programa calcula o preço a pagar por um carro alugado.

dia = int(input('Quantos dias alugados: '))
km = float(input('Qual a quantidade de kms rodados: '))
pago = (dia * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(pago))
