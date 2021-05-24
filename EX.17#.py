#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo,calcule e mostre
#o comprimento da hipotenusa

from math import hypot
catop=float(input('Qual o comprimento do cateto oposto:'))
catad=float(input('Qual o comprimento do cateto adjacente:'))
hip= hypot(catop,catad)
print('a sua hipotenusa vai medir:{:.2f}'.format(hip)))
