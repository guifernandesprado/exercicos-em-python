#Esse programa lê o comprimento de três segmentos de reta e informa se eles podem ou não formar um triângulo. Se puderem, informa qual tipo de triângulo será formado: equilátero, isósceles ou escaleno.


r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2+r3 and r2 < r3+r1 and r3 < r1+r2:
    print('Os segmentos acima podem formar um triângulo ',end='')
    if r1 == r2 == r3 :
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
            print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos acima não podem formar triângulo!')
