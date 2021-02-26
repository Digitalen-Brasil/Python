# Recebe a entrade de 3 números e diz se estão em ordem crescente ou não

a = int(input('Digite o primeiro número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))
c = int(input('Digite o terceiro número inteiro: '))

crescente = a < b < c

if crescente == True:
    print('crescente')
else:
    print('não está em ordem crescente')