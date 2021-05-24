#O professor quer sortear a ordem de apresentação de trabalhos dos
#alunos.Faça um programa que leia o nome dos quatro alunos e mostre
#a ordem solicitada.

from random import shuffle
a1=input('Digite o seu nome:')
a2=input('Digite o seu nome:')
a3=input('Digite o seu nome:')
a4=input('Digite o seu nome:')
lista=[a1,a2,a3,a4]
sorteio=shuffle(lista)
print('a Sequência do Sorteio foi:{}'.format(lista,sorteio))
