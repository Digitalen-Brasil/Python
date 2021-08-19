# Criar um programa que converte um valor em metros para centímetros e milímetros
# Desafio 8 da aula 7

def base_metros():
	print("\nVocê escolheu converter a partir de metros")
	
	metros = float(input("Digite o valor em metros: "))
	
	met_cen = metros*100
	met_mil = metros*1000
	print(f"{metros} metros é igual a {met_cen} centímetros e {met_mil} milímetros")
	
	encerramento()
		
def base_centimetros():
	print ("\nVocê escolheu converter a partir de centímetros")
	
	centimetros = float(input("Digite o valor em centímetros: "))
	
	cen_met = centimetros/100
	cen_mil = centimetros*10
	
	print(f"{centimetros} centímetros é igual a {cen_met} metros e {cen_mil} milímetros.")
	
	encerramento()
	
	
def base_milimetros():
	print ("\nVocê escolheu converter a partir de milímetros")
	
	milimetros = float(input("Digite o valor em milímetros: "))
	
	mil_cen = milimetros/10
	mil_met = milimetros/1000
	
	print(f"{milimetros} milímetros é igual a {mil_met} metros e {mil_cen} centímetros.")
	
	encerramento()
	
def encerramento():
	encerrar = int(input("\nDeseja fazer novas conversões? Se SIM digite 1, se NÃO digite 2: "))
	
	if encerrar == 1:
		main()
	if encerrar == 2:
		print("Obrigado por utilizar nosso programa!")
	if encerrar != 1 and encerrar != 2:
		print("Por gentileza digite 1 para continuar no programa e 2 para encerrar")
		encerramento ()

def main():
	inicio = int(input("\nEscolha a opção que você deseja converter:\n1 - Valor inicial em metros\n2 - Valor inicial em centímetros\n3 - Valor inicial em milimetros\nDigite o número da opção desejada: "))
	if inicio == 1:
		base_metros()
	if inicio == 2:
		base_centimetros()
	if inicio == 3:
		base_milimetros()
		
	if inicio != 1 and inicio != 2 and inicio != 3:
		print("\nEscolha uma opção entre 1, 2 e 3\n")
		main()
		
main()
