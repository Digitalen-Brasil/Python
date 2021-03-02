## SOLUÇÃO COMPLEXA! PROCURAR FORMA MAIS SIMPLES

n = int(input('Digite um número inteiro: '))

if n == 2 or n == 3 or n == 5 or n == 7 :
    print('primo')

else:

    par = n % 2 == 0 #True ou False
    ultimoZero = n % 10 == 0
    ultimoCinco = n % 10 == 5

    soma = 0

    while (n > 0):
        soma += n % 10
        n = n // 10
        resultado = soma
        porTres = resultado % 3 == 0
        porSete = resultado % 7 == 0



    if not par and not porTres and not porSete and not ultimoZero and not ultimoCinco:
        print('primo')
    else:
        print('não primo')
