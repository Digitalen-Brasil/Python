# Receber uma lista, verificar valores repetidos e remove-los.
# Imprimir a nova lista em ordem crescente

# A função está recebendo como parâmetro um objeto chamado "lista"
def remove_repetidos(lista):
    clone = []

    # Para cada objeto na lista, vai criar uma variável N de cada número
    for i in lista:
        n = i
    # Enquanto N estiver na lista, e ainda não estiver na clone, vai ser inserido na clone
        while n in lista and not n in clone:
            clone.append(i)
    # O comando Sorted vai por os itens em ordem
    return sorted(clone)

