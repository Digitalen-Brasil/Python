lista = [] #Lista vazia

n = int(input('Digite um valor inteiro. Digite zero para encerrar: '))

while n != 0: #Enquanto o valor digitado não for 0
    # Comando ".append()" adiciona o item a lista
    lista.append(n)
    n = int(input('Digite um valor inteiro. Digite zero para encerrar: '))

# Comando ".reverse()" inverte a posição dos itens na lista
lista.reverse()
print(lista)