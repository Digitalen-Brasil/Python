meuCartao = int(input('Digite o número do seu cartão de crédito: '))
cartaoLido = 1
cartaoLista = False

# Esse programa usa o "and not" ou seja, enquanto cartaoLista for falso.
while (cartaoLido != 0 and not cartaoLista):
    cartaoLido = int(input('Digite o número do cartão que deseja comparar. '
                           'Digite zero para encerrar o programa: '))
    if cartaoLido == meuCartao:
        cartaoLista = True # Indicador de passagem vai transformar o cartaoLista em True.

if cartaoLista:
    print('Cartão está na lista!')
else:
    print('Cartão não está na lista')