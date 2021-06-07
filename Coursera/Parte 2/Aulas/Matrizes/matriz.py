def cria_matriz(num_linhas,num_colunas,valor):
    ''' (int, int, valor) -> Cria uma matriz (lista de listas)
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
            linha.append(valor)

        # Adiciona linha a matriz
        matriz.append(linha)

    print(matriz)
    return matriz

def main():
    cria_matriz(5,8,0)

main()
