# Programa que vai ler um input, e dizer o contéudo dela.

variavel = input('Digite algo: ')
num = variavel.isnumeric()
alfanum = variavel.isalnum()
text = variavel.isalpha()
espacos = variavel.isspace()
primeira_maiscula = variavel.istitle()
tudo_maiscula = variavel.isupper()

# Usando uma formatação de texto do Python 3.6
print(f'\nA variavel é:\nNúmerica? {num}\nAlfa-Númerica? {alfanum}\nSomente texto? {text}\n'
      f'Espaços em branco? {espacos}\nÉ texto e tem a primeira letra maiúscula? {primeira_maiscula}\n'
      f'É texto e está todo em maiúscula? {tudo_maiscula}')