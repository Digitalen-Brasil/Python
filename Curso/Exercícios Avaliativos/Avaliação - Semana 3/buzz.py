# Imprime "Buzz" se o número for divisível por 5

num = int(input('Digite o número que deseja saber se é divisível por 5: '))
div = num % 5

if div == 0:
    print('Buzz')
else:
    print(num)