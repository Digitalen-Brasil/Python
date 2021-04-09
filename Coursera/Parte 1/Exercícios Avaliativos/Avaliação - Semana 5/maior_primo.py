def maior_primo(n):
    for k in range(n, 1, -1):
        if éPrimo(k):
            return k

def éPrimo(k):
    div = 1 # Divisor
    cont = 0 # Contador de divisões
    while k >= div: # Enquanto K > ou igual ao divisor
        if k % div == 0: # Se a sobra de K/Divisor for igual a zero
            cont += 1 # Aumenta um número ao contador de divisões
        div += 1 # Se a sobra da divisão não for 0, aumenta um divisor
        if cont > 2: # Se for possível dividir o número mais de 2 vezes, ele não é primo
            return False
    return True