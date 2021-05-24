#Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno,cosseno e tangente desse ângulo

from math import radians,sin,cos,tan
ang=float(input('Digite o ângulo que você deseja:'))
seno=sin(radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang,seno))
cosseno=cos(radians(ang))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(ang,cosseno))
tangente=tan(radians(ang))
print('o ângulo de {} tem a tangente de {:.2f}'.format(ang,tangente))
