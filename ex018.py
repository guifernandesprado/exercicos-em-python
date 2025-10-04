#Esse programa lê o nome completo de uma pessoa e mostra o primeiro e o último nome separadamente.

n = str(input('Digite se nome completo : ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))