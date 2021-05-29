'''Crie um programa que leia um número inteiro e mostre na tela
 se ele é PAR ou ÍMPAR'''

num=int(input('Digite um número qualquer:'))
resultado=num%2
if resultado == 1:
    print('Esse número {} é IMPÁR'.format(num))
else:
    print('Esse número {} é PAR'.format(num))
