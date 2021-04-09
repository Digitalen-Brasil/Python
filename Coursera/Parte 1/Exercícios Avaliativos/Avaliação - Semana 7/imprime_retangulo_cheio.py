def impressao(x,y):
    linhas = 1
    while y >= linhas:
        linhas += 1
        print('#'*x)

def main():
    # X = Largura
    # Y = Altura
    x = int(input('digite a largura: '))
    y= int(input('digite a altura: '))

    if x > 0 and y > 0:
        impressao(x,y)

main()