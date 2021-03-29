#Faz o cálculo fatorial, e retorna para a chamada
def fatorial(n,fact):
    while n >= 1:
        fact = fact * n
        n = n - 1
    print(fact)
    chamada()

#Vai receber o número. Se for negativo, encerra a aplicação, se for positivo segue para o fatorial
def chamada():
    n = int(input('Digite um número inteiro: '))
    fact = 1

    if n < 0:
        print('\nA aplicação será encerrada. Obrigado')
    else:
        fatorial(n,fact)

chamada()
