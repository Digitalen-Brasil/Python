# Crie um programa que leia um número e mostre seu antecessor e seu sucessor
# Desafio 5 da aula 7

"""
O Programa começa com a função 'Main()' que fica no final do código.
As funções ANTECESSOR e SUCESSOR vão realizar os calculos diretamente do 'return'
No 'Main()' o programa chama as funções 'antecessor(num)' e 'sucessor(num)' diretamente do print
"""

def antecessor(num):
    return num - 1

def sucessor(num):
    return num + 1

def main():
    num = int(input('Por favor, digite um número inteiro: '))
    print(f'Número digitado {num}: Seu antecessor é {antecessor(num)}, e seu sucessor é {sucessor(num)}')

main()

