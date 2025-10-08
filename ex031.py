#Esse programa lê as duas notas de um aluno, calcula e mostra a sua média.

n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))
média = (n1 + n2) / 2
if média < 5:
    print('Sua média foi de {} , você foi REPROVADO!'.format(média))
elif média <6.9:
    print('Sua média é de {} , você está de RECUPERAÇÃO! '.format(média))
elif média >= 7 :
    print('Sua média é de {} , PARABÉNS, VOCÊ FOI APROVADO!'.format(média))