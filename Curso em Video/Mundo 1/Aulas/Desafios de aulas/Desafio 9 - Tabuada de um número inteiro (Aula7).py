#Ler um número inteiro e mostrar a tabuada dele
#Desafio 9 da aula 07

def tabuada(numero):
	
	i = 1
	while i <= 10:
		num = numero * i
		print(f"{numero} x {i} = {num}")
		i += 1

def main():
	numero = int(input("Digite um número para mostrar a tabuada dele: "))
	tab = tabuada(numero)
	
main()