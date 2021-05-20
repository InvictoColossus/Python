# Faça um algorítmo que leia o valor do produto,
# e mostre na tela pagando a vista 10%
#de Desconto e parcelado 10% de aumento.Meu teste..

Produto=float(input('Digite o valor do produto:R$:'))
Desconto=Produto - (Produto*10/100)
Aumento=Produto + (Produto*10/100)
print('O valor do Produto é R$:{:.2f} Pagando a Vista você tem um desconto de 10% e fica R$:{:.2f}'.format(Produto,Desconto))
print('O valor do produto é R$:{:.2f} Parcelando ele tem um aumento de 10% e fica R$:{:.2f}'.format(Produto,Aumento))
