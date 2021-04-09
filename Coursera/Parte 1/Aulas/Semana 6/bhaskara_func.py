# Programa para encontrar raiz quadrada de uma função de segundo grau
import math

print('A forma geral da equação de segundo grau é: \033[1max² + bx - c = 0\033[m'
      '\n"a", "b" e "c" são os valores constantes da equação, ou seja, os valores conhecidos.\n')

def delta(a, b, c): # Define a função para calcular Delta
    return (b ** 2) - (4 * a * c)
+

def main():
    # Entrada das constantes pelo usuário
    a = float(input('Qual o valor de "a"? '))
    b = float(input('Qual o valor de "b"? '))
    c = float(input('Qual o valor de "c"? '))
    imprime_raizes(a,b,c)

def imprime_raizes(a, b, c):
    d = delta(a,b,c)
    if d == 0:
        zero = (-b + math.sqrt(d)) / (2 * a)
        print('a raiz desta equação é {}'.format(zero))

    else:
    # Não existe raiz quadrada de número negativo, logo, não existem soluções reais para o problema
        if d < 0:
            print('esta equação não possui raízes reais')
        else:
            # Fórmula para encontrar o primeiro X é: x = (-b + Raiz Quadrada de Delta) / (2.a)
            x = (-b+math.sqrt(d))/(2*a)
            # Fórmula para encontrar o primeiro X é: x = (-b - Raiz Quadrada de Delta) / (2.a)
            y = (-b-math.sqrt(d))/(2*a)
            print('as raízes da equação são {} e {}'.format(x,y))


