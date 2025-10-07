#Esse programa lê o comprimento de três segmentos de reta e informa se eles podem ou não formar um triângulo.

cores = {'limpa' : '\033[m ',
         'azul' : '\033[34m' ,
         'amarelo' : '\033[33m' ,
         'pretoebraco' : '\033[7;30'}
print('\033[34m-=\033[m' * 30)
print('\033[4;33mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[34m-=\033[m' * 30)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2+r3 and r2 < r3+r1 and r3 < r1+r2:
    print('\033[1;32;47mOs segmento acima podem formar triângulo!\033[m')
else:
    print('\033[1;31;47mOs segmento acima não podem formar triângulo!\033[m')
