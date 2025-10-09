

altura = float(input('Digite sua altura: (m) '))
peso = float(input('Digite seu peso: (kg) '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5 :
    print('Abaixo do peso.')
elif imc < 25 :
    print('Peso Normal')
elif imc < 30 :
    print('Sobrepeso')
elif imc < 40 :
    print('Obesidade')
else:
    print('Obesidade mórbida')