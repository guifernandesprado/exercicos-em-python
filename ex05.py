#Esse exercício lê a largura e a altura de uma parede em metros, calcula a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg=float(input('Largura da parede:'))
alt=float(input('Altura da parede:'))
área=larg*alt
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}m²'.format(larg,alt,área))
tinta=área/2
print('Para pintar essa parede você,pracisará de {}l de tinta.'.format(tinta))
