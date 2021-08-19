# Programa para ler duas notas e calcular médias
# Desafio 6 da aula 7

def medias(notas, testes, nota_corte):
    """
    A média final é calculada somando todas as notas dentro da lista  e dividido pela quantidade de testes definidos
    """
    media_final = sum(notas) / testes

    # A resposta final ao usuário vai depender se a média final é menor que a nota de corte ou maior.
    if media_final < nota_corte:
        print(f'\nA média {media_final:.2f} é mais baixa que a nota de corte. \033[1mREPROVAÇÃO\033[m')
    else:
        print(f'\nA média {media_final:.2f} é maior que a nota de corte. \033[1mAPROVAÇÃO\033[m')

def main():

    testes = int(input('Quantas notas serão avaliadas na média? Mínimo de 2 notas: '))
    notas = [] # Uma lista vazia que vai receber os números das notas
    maxLengthList = testes # O tamanho máximo da lista vai ser a quantidade de avaliações que foi digitada

    nota_corte = float(input('Qual a nota mínima para aprovação? '))
    while len(notas) < maxLengthList:
        """ 
        Enquanto o comprimento da lista 'notas' for menor que a quantidade de avaliações, 
        a lista vai continuar recebendo valores
        """
        num = float(input('Por favor, digite a nota (utilize ponto "." no lugar de vírgulas): '))
        notas.append(num)
        testes+1

    media = medias(notas,testes,nota_corte)

main()