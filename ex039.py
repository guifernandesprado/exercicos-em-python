#Esse programa mostra a soma de todos os números ímpares que são múltiplos de 3 e que estão no intervalo de 1 a 500

soma = 0
cont = 0
for n in range (1,501,2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
print('A soma de todos os {} valores solicitados é de {}.'.format(cont,soma))