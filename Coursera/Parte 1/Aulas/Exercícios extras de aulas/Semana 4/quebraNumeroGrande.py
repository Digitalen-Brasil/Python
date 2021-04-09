# Programa que vai receber um número grande, quebrar ele em unidades e somar elas
numero = int(input('Digite o número inteiro: ')) # Vai receber o número dos usuários
soma = 0 # A soma começa com 0

while (numero > 0): # Sempre que o número digitado pelo usuário for maior que 0:
# Esse comando vai buscar o valor de "numero" e enquanto ele não for 0 vai repetindo a ação.
    
    # A soma vai receber o valor do último digito em "numero", e ir somando
    soma += numero % 10
    # Vai tirar o último digito de número, e devolver para a "soma"
    numero = numero // 10

print(soma)

