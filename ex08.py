#Esse programa converte uma temperatura digitada em °C e converte para °F.

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5 ) + 32
print ('A temperatura de {} °C conresponde a {} em °F!'.format(c,f))