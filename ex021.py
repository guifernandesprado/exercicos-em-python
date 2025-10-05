#esse exercício calcula o preço de uma passagem de acordo com a distância da viagem.

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} km!'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem é de R${:.2f}.'.format(preço))
print('Boa Viagem!')