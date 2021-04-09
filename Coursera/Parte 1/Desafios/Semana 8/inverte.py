def inverter(lista):

    # Essa função reverte a ordem que a lista foi inserida
    lista.reverse()

    # O for irá percorrer os itens (i) na lista que foi invertida, e imprimi-los
    for i in lista:
        print(i)

    return i

def main():
    n = 1 # Input para iniciar o laço
    lista = [] # Lista Vazia

    # Enquanto o usuário não digitar o 0
    while n != 0:
        n = int(input('Digite um número: '))

        # Se o número digitado não for zero, é adicionado a lista.
        if n != 0:
            lista.append(n)

    # Se o número digitado for zero vai chamar a função inverter
    inverter(lista)

    # Vai enviar o valor da lista
    return lista

main()