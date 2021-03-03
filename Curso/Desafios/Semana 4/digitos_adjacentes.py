numero = int(input('Digite um número inteiro: '))

sobra_anterior = numero % 10
inteiro_atual = numero // 10
adja = False
x = 0

while (inteiro_atual > 0 and not adja):
    sobra_atual = inteiro_atual % 10

    if sobra_atual == sobra_anterior:
        adja = True
    else:
        x += 1
    sobra_anterior = sobra_atual
    inteiro_atual = inteiro_atual // 10

if adja:
    print('sim')
else:
    print('não')