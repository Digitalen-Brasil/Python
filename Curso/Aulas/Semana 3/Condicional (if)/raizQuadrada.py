# Programa para encontrar raiz quadrada de uma função de segundo grau
import math

# O código \033[m é utilizado para editar o formato e cor do texto.
# Nessa atividade, está colocando as palavras em negrito
print('A forma geral da equação de segundo grau é: \033[1max² + bx - c = 0\033[m'
      '\n"a", "b" e "c" são os valores constantes da equação, ou seja, os valores conhecidos.\n')

# Entrada das constantes pelo usuário
a = float(input('Qual o valor de "a"? '))
b = float(input('Qual o valor de "b"? '))
c = float(input('Qual o valor de "c"? '))

# Calculo do delta, utilizando a formula: Delta = b² - 4.a.c
delta = (b**2) - (4*a*c)

# Não existe raiz quadrada de número negativo, logo, não existem soluções reais para o problema
if delta < 0:
    print('\033[1mNão há raizes reais\033[m')

# Se Delta for maior que é, é calculado X' e X'', ou x e y.
# O comando para calcular raiz quadrada no módulo math é: "math.sqrt()"
if delta > 0:
    # Fórmula para encontrar o primeiro X é: x = (-b + Raiz Quadrada de Delta) / (2.a)
    x = (-b+math.sqrt(delta))/(2*a)
    # Fórmula para encontrar o primeiro X é: x = (-b - Raiz Quadrada de Delta) / (2.a)
    y = (-b-math.sqrt(delta))/(2*a)

    print("X' é igual a \033[1m{}\033[m e X'' é igual a \033[1m{}\033[m".format(x,y))

if delta == 0:
    # Quando delta é igual a zero, só existe uma solução real, encontrada pela fórmula: x = (-b+delta)/2
    zero = (-b+delta)/(2*a)
    print('A única solução real é \033[1m{}\033[m'.format(zero))