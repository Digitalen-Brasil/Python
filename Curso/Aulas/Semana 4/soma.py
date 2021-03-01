# Vai pegar a soma de uma sequência de números
print("Digite uma sequência de valores para somar. Para encerrar, digite 0")
soma = 0
valor = 1

while (valor != 0):
    valor = int(input("Digite o valor a ser somado "))
    soma = soma + valor

print('A soma dos valores digitados é {}'.format(soma))