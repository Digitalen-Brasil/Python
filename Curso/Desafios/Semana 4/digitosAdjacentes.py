# Desafio para encontrar números adjacentes iguais
## EXERCICIO AINDA SEM COMPREENSÃO TOTAL

numero = n = int(input('Digite o número que você deseja analisar: '))

ultimo = numero % 10
n = numero // 10

adjIguais = False
contagemIguais = 0

while (n > 0 and not adjIguais):
    atual = n % 10
    if atual == ultimo:
        adjIguais = True
    else:
        contagemIguais += 1
    ultimo = atual
    n = n // 10

if adjIguais:
    print(numero, "tem dois digitos", atual, "adjacentes")
else:
    print(numero, "nao tem digitos iguais adjacentes")



