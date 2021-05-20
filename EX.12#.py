#Faça  Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o preço do Produto? R$:'))
novo = preço - (preço * 5 / 100)
print('O preço do produto é {:.2f} com o desconto fica R${:.2f}'.format(preço,novo))
