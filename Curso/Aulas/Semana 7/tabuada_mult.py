linha = 1
coluna = 1

while linha <= 10: # Vai testar se a linha é menor ou igual a 10
    print("A tabuada de {} é: ".format(linha), end="\t")
    while coluna <=10: # Se a linha for igual ou menor a 10, vai testar se a coluna é <= 10.
        tabuada = linha * coluna # Se o segundo WHILE for verdadeiro, vai executar o comando.
        print(tabuada, end='\t')
        coluna += 1 # Adiciona mais um a coluna, e o programa continua testando os DOIS WHILE!
    linha += 1 # Adiciona uma nova linha, já que o programa continua testando o WHILE original
    print()
    coluna = 1 # Reinicia o número de colunas, para continuar a multiplicação enquanto linha for <= 10