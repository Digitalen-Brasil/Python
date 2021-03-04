import math

n = int(input('Digite um número inteiro, positivo, para N: '))
k = int(input('Digite um número inteiro, positivo e menor que n, para K: '))

def entrada():
    n = int(input('Digite um número inteiro, positivo, para N: '))
    k = int(input('Digite um número inteiro, positivo e menor que n, para K: '))

while (k > n):
    print('K deve ter um valor menor que N')
    break
else:
    def fatorial (x):
        return math.factorial(x)

    calculo = fatorial(n)//(fatorial(k)*fatorial(n-k))

    print(calculo)