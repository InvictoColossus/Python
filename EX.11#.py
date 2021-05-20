# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura=float(input('digite a largura da parede:'))
altura=float(input('digite a altura da parede:'))
area=largura * altura
print('a sua parede tem dimensão de {} x {} \n e sua área é {}'.format(largura,altura,area))
tinta = area / 2
print('Para pintar esta parede você precisará de {}l de tinta'.format(tinta))
