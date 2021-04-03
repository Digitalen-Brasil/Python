def primos(x):
    fator = 2

    while x % fator !=0 and fator <= x/2:
        fator += 1
    if x % fator != 0 or x == 2:
        return True
    else:
        return False

def n_primos(x):
    i = 2
    soma = 0

    while i <= x:
        if primos(i):
            soma += 1
        i = i + 1
    return soma


n_primos(121)