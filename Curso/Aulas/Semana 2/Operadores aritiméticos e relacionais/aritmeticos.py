# Operadores aritméticos

print(' \033[1mSão operadores aritméticos:\033[m \n + -> Soma \n - -> Subtração \n * -> Multiplicação \n \ -> Divisão \n ** -> Potenciação \n '
      '// -> Parte inteira de uma divisão \n % -> Resto da divisão \n == -> Igualdade'
      '\n != -> Diferente de (...)')

print('-----------------------------------------------------------')
print ('\033[2mExemplos:\033[m')

print('O que você deseja ver um exemplo? '
              '\n (1) Soma, '
              '(2) Subtração, '
              '(3) Multiplicação, '
              '(4) Divisão, '
              '(5) Potencialização, '
              '\n (6) Parte inteira da divisão, '
              '(7) Resto da divisão, '
              '(8) Igualdade, '
              '(9) diferente de... ')
opcao = str(input('\nDigite o número correspondente: '))


# Ação para somar
if opcao == '1':

    soma1 = int(input('\nDigite o primeiro valor: '))
    soma2 = int(input('Digite o segundo valor: '))
    somares = soma1 + soma2
    print(('{} + {} = {}'.format(soma1, soma2, somares)))

# Ação para subtrair
elif opcao == '2':

    subtr1 = int(input('\nDigite o primeiro valor: '))
    subtr2 = int(input('Digite o segundo valor: '))
    subtres = subtr1 - subtr2
    print('{} - {} = {}'.format(subtr1, subtr2, subtres))

# Ação para multiplicação

elif opcao == '3':

    mult1 = int(input('\nDigite o primeiro valor: '))
    mult2 = int(input('\nDigite o primeiro valor: '))
    multres = mult1 * mult2
    print('{} x {} = {}'.format(mult1, mult2, multres))

# Ação para divisão

elif opcao == '4':
    divi1 = int(input('\nDigite o primeiro valor: '))
    divi2 = int(input('\nDigite o primeiro valor: '))
    divres = divi1 / divi2
    print('{} / {} = {}'.format(divi1, divi2, divres))

# Ação para potenciação

elif opcao == '5':
    pote1 = int(input('\nDigite o primeiro valor: '))
    pote2 = int(input('\nDigite o primeiro valor: '))
    poteres = pote1 ** pote2
    print('{} ** {} = {}'.format(pote1, pote2, poteres))

# Ação para número inteiro de divisão

elif opcao == '6':

    intd1 = int(input('\nDigite o primeiro valor: '))
    intd2 = int(input('\nDigite o primeiro valor: '))
    intdres = intd1 // intd2
    print('{} dividido por {} tem como número inteiro {}'.format(intd1, intd2, intdres))

# Ação para encontrar o resto da divisão

elif opcao == '7':

    resd1 = int(input('\nDigite o primeiro valor: '))
    resd2 = int(input('\nDigite o primeiro valor: '))
    resres = resd1 % resd2
    print('Entre {} e {}, o valor restante é {}'.format(resd1, resd2, resres))

# Ação para descobrir se é igual ou não

elif opcao == '8':

    igu1 = int(input('\nDigite o primeiro valor: '))
    igu2 = int(input('\nDigite o primeiro valor: '))
    igures = igu1 == igu2
    print('{} e {} são iguais? {}'.format(igu1, igu2, igures))

# Ação para descobri se são diferentes

elif opcao == '9':

    dif1 = int(input('\nDigite o primeiro valor: '))
    dif2 = int(input('\nDigite o primeiro valor: '))
    difres = dif1 != dif2
    print('{} e {} são diferentes? {}'.format(dif1,dif2, difres))