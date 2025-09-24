#Esse exercício lê um número inteiro e mostra na tela o seu dobro, triplo e raiz quadrada.
#Ex: Digite um número: 5

n1= int(input('Digite um número:'))
n2= n1*2
n3= n1*3
n4= n1**2
print('Voce digitou o número {}, sendo assim seu dobro é de {}, seu triplo é {} e sua raiz quadrada é {}.'.format(n1,n2,n3,n4))