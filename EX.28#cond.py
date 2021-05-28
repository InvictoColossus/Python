'''Escreva um programa que faça o computador “pensar” em um número
 inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import  randint
from time import  sleep
computador=randint(0,5)    #computador pensando número
print('-=-'*20)
print('Tente Acertar o número que eu pensei...:')
print('-=-'*20)
jogador=int(input('Em que número vc pensou...')) #jogando tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS!!Vc me Venceu....')
else:
    print('VC errou o número que eu pensei foi {} e não o {}'.format(computador,jogador))
