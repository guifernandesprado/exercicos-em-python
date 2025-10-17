#Esse programa mostra a tabuada de um número que o usuário escolher

n = int(input('Digite um número e veja sua tabuada: '))
for c in range (1,11):
    print('{} x {} = {}'.format(n,c,n*c))