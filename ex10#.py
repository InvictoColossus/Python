n=float(input('Quanto dinheiro vc tem na carteira?R$:'))
euro=n/6.45
dolar=n/5.27
print('Com R${:.2F} Você pode Comprar US$ {:.2f}'.format(n,euro))
print('com R${:.2F} você pode comprar ${:.2f}'.format(n,dolar))
