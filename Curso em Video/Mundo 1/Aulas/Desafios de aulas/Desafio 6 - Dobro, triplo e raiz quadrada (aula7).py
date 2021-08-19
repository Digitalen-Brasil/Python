# Programa para ler um número e dar o seu dobro, triplo e raiz quadrada
# Desafio 6 da aula 7

"""
O programa começa a funcionar com a função 'main()' no final do código.
Foi importado da biblioteca MATH o comando 'sqrt' que serve para calcular a raiz quadrada.
"""

from math import sqrt

def dobro(num): # Calcula o dobro do número digitado
    return num * 2

def triplo(num): # Calcula o triplo do número digitado
    return num * 3

def raiz(num): # Utiliza o comando 'sqrt' da biblioteca MATH e calcula a raiz quadrada.
    return sqrt(num)

def main():
    """ 'num' recebe o número do usuário e o print chama as funções diretamente dos colchetes """

    num = int(input('Digite um número de valor inteiro: '))
    print(f'O número digitado foi {num}: O dobro desse número é {dobro(num)}, o triplo é {triplo(num)} e a raiz quadrada é {raiz(num):.2f}')

main()
