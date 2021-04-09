# O programa vai ler dois números inteiros
# Se o primeiro número for maior que o segundo, exibir: MAIOR
# Se os dois números forem iguais, exibir: IGUAIS
# Se o primeiro número for menor que o segundo, exibir: MENOR

def comparacao(a,b):
    if a > b:
        print('\nMaior')
    elif a < b:
        print('\nMenor')
    else:
        print('\nIguais')
    return

def main():
    a = int(input('Digite o primeiro número inteiro: '))
    b = int(input('Digite o segundo número inteiro: '))
    comparacao(a,b)

    continuar = int(input('\nDeseja fazer outra Comparação?\nSe sim, digite 1.\nSe não, digite 2.\n-> '))
    print('')

    if continuar == 1:
        main()
    elif continuar == 2:
        print('\033[1mObrigado por usar nosso programa\033[m')
        return
    else:
        print('Opção inválida')
        print('Vamos encerrar o programa, obrigado!')

main()
