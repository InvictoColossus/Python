''' Desenvolva um programa que pergunte a distância de uma viagem
 em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
  para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia=float(input('Qual a distancia da sua viagem?'))
print('Vc está prestes a comecar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco=distancia*0.50
else:
    preco=distancia*0.45
print('O preço a sua viagem será R$:{:.2f}'.format(preco))
