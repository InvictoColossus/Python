#Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

celsius=float(input('Digite a Temperatura C:'))
Fahre=((celsius*9) / 5) + 32
print('A temperatura em Celsius foi C:{}\n Convertendo para Fahrenheit fica F:{}'.format(celsius,Fahre))
