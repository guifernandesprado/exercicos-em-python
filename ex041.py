# esse programa lê 6 números inteiros e mostra a soma apenas daqueles que forem pares

soma = 0
cont = 0
for c in range (1,7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 ==0:
        soma += num
        cont += 1
print('Você informou {} números PARES e soma deles foi de {}.'.format(cont,soma))