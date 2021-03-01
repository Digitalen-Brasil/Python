# Exércicio para achar uma sequência de números multiplicados
print('Digitar uma sequência de números, e fazer uma multiplicação entre eles\n')

# Vai perguntar a quantidade de vezes que o usuário quer digitar os números
quant = int(input('Qual a quantidade de números que você gostaria de multiplicar? '))
maximo = 1 # Valor minimo de vezes. Se o usuário digitar 0, o comando While entende como falso e não cria os laços

produto = 1 # Valor base da multiplicação. Nesse caso o valor digitado * 1

while (maximo <= quant): # Enquanto o maximo for igual ou menor que a quantidade desejada...
    valor = int(input('Digite o valor a ser multiplicado: '))
    produto = produto * valor # Multiplica o produto (1) pelo valor digitado do usuário
    maximo += 1 # Vai somando mais 1 no maximo, até chegar na condição pedida do while.

print('A multiplicação é {}'.format(produto))