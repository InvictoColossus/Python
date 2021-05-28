''' Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade=float(input('Qual a velocidade do carro:'))
if velocidade > 80:
    print('MULTADO!!Você excedeu o limite permitido que era de 80/h')
    multa=(velocidade-80)*7
    print('A sua multa foi de {:.2f}'.format(multa))
    print('-=-'*20)
print('Tenha um Bom Dia!!Diriga com Segurança')
