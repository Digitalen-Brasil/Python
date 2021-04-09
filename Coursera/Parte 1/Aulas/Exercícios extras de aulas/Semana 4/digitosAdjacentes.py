# Desafio para encontrar números adjacentes iguais
## ATUALIZADO COM DEBUG APRENDIDO NO DESAFIO DA SEMANA 4

numero = int(input('Digite o número que você deseja analisar: '))

sobraAntiga = numero % 10
inteiro = numero // 10

adjIguais = False
contagemIguais = 0

while (inteiro > 0 and not adjIguais):
    atual = inteiro % 10
    if atual == sobraAntiga:
        adjIguais = True
    else:
        contagemIguais += 1
    sobraAntiga = atual
    inteiro = inteiro // 10

if adjIguais:
    print(numero, "tem dois digitos", atual, "adjacentes")
else:
    print(numero, "nao tem digitos iguais adjacentes")



