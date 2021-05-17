nome = input('qual é o seu nome?')
print(nome,'prazer em conheço-lo.')

dia=input('qual seu dia de aniversário?')
mes=input('qual seu mes de aniversário?')
ano=input('qual seu ano de nascimento?')
print('voce nasceu no',dia,'no mes',mes,'no ano de',ano)


numero1=int(input('Digite o primeiro numero:'))
numero2=int(input('Digite o segundo numero:'))
soma=numero1+numero2
#print('a soma entre', numero1 ,'e',numero2,'é',soma)
print('a soma entre {} e {} vale {}'.format(numero1,numero2,soma))
