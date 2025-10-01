#Esse programa calcula a hipotenusa de um triângulo retângulo

'''co = float(input('Comprimento do cateto oposto: '))
ca= float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2 ) **(1/2)
print('A hipotenusa vai medir {:.2f} .'.format(hi))'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('O valor da hipotenusa é de {:.2f} .'.format(hi))