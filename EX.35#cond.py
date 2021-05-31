
'''Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo.'''
print('-=-'*20)
print('Analisador de Triângulo')
print('-=-'*20)
r1=float(input('Digite a reta do triângulo:'))
r2=float(input('Digite a segunda reta:'))
r3=float(input('digite a terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima podem formar Triângulo')
else:
    print('Os Segmentos acima não podem formar Triângulo')
