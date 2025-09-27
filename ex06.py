#Esse exercício calcula o desconto de 5% em um produto.

preço = float(input('Qual é o preço do produto R$'))
novo = preço - (preço *5 / 100)
print('O produto que custa R${:.2f}, na promoção com desconto de 5% irá custar R${:.2f}.'.format(preço,novo))