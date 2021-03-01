# Programa para encontrar potências de 2
# O programa poderia ser escrito de forma bruta da seguinte maneira:
# print(2 ** 0)
# print(2 ** 1)
# print(2 ** 2)
# (...)
# Nesse exemplo a parte "print(2 ** (...) )" é fixa
# O comando While pode criar uma repetição para deixar essa parte fixa,
# e alterar somente a variável

# i é a parte variável
i = 0

# A repetição nesse exemplo vai terminar quando a variável tiver o valor igual a 10
while (i <= 10):
    i += 1 # Serve para adicionar +1 a variável toda vez que ela é testada na condição
    print(2 ** i)
    
