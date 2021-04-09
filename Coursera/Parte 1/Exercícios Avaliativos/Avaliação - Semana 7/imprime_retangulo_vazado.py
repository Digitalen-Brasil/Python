def impressao(x,y):
    linhas = 1
    vazios = (x-2) * ' ' # Vai inserir os espaços vazios na linha

    print('#'*x) # Primeira linha - Cheia

    # Vai preencher o meio com as linhas vazias.
    # Enquanto a altura original, menos 1, for maior que a quantidade de linhas
    while (y-1) > linhas:
            print('#{}#'.format(vazios))
            linhas += 1

    print('#' * x) # Ultima linha - Cheia

def main():
    #X = Largura
    #Y = Altura

    x = int(input('digite a largura: '))
    y= int(input('digite a altura: '))

    if x > 0 and y > 0:
        impressao(x,y)

main()

