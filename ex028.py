#Esse programa lê dois números e mostra qual é o maior ou se são iguais.

primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))
if primeiro > segundo :
    print('O primeiro número é maior!')
elif primeiro < segundo :
    print('O segundo número é maior!')
else :
    print('Os dois valores são iguais!')
