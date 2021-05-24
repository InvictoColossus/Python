#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele,lendo o nome deles
# e escrevendo o nome escolhido.


import random
a1=input('Digite o seu nome:')
a2=input('Digite o seu nome:')
a3=input('Digite o seu nome:')
a4=input('Digite o seu nome:')
lista=[a1,a2,a3,a4]
sorteio=random.choice(lista)
print('O Sorteio entre os alunos {},{},{} e {} \nfoi sorteado o aluno:{}'.format(a1,a2,a3,a4,sorteio))
