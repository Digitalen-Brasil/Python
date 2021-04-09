# Programa para receber um número inteiro e responder se é par ou ímpar

numero = int(input('Digite um número inteiro: '))
par = numero % 2

if par == 0:
    print('par')

else:
    print('impar')