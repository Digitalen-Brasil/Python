# Imprime "Fizz" se o número for divisível por 3

num = int(input('Digite o número que deseja saber se é divisível por 3: '))
div = num % 3

if div == 0:
    print('Fizz')
else:
    print(num)