def cria_matriz(num_linhas,num_colunas):
    ''' (int, int) -> Cria uma matriz (lista de listas)
    num_linhas -> Vai armazenar um valor inteiro (int) com o número de linhas
    num_colunas -> Vai armazenar um valor inteiro (int) com o número de colunas '''

    matriz = [] # Lista Vazia
    for i in range(num_linhas):
        ''' Dentro do número de linhas, 
        a função vai buscar cada elemento até chegar no final do (num_linhas)'''
        # cria linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            ''' Dentro do range (num_colunas) vai adicionar as linhas'''
            valor = int(input(f'Digite o valor do item na linha {i} e coluna {j}: '))
            linha.append(valor)

        # Adiciona linha a matriz
        matriz.append(linha)

    return impressão(matriz, num_linhas,num_colunas)

def impressão(matriz,num_linhas,num_colunas):
    """Para imprimir no formato visual correto.
    """
    for i in range(num_linhas):
        for j in range(num_colunas):
            print(f'[{matriz[i][j]:^5}]',end=' ')
        print()


def main():
    lin = int(input('Digite o número de linhas: '))
    col = int(input('Dgite o número de colunas: '))
    cria_matriz(lin,col)

main()