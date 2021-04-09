# Programa para testar um indicador de passagem,
# indicando se a sequência é decrescente ou não

# Usuário digita um valor inicial, esse valor é registrado como "anterior"
anterior = int(input('Digite o primeiro valor da sequência: '))
decrescente = True # Decresente já é considerado como padrão
valor = 1 # Um valor pré estabelecido para gerar condições no while

# Enquanto valor não for zero, e descrente for True:
# O 'decrescente' já está considerado como True pois é o padrão dele.
# Isso é um indicador de passagem
while valor!=0 and decrescente:
    valor = int(input('Digite o próximo número da sequência: '))

# No momento em que o valor for maior q o número anterior, o decresente muda para False
    if valor > anterior:
        decrescente = False

# Se o número atual não for maior, ele é automaticamente setado como anterior
    anterior = valor

if decrescente:
    print('A sequência está em ordem decrescente!')
else:
    print('A sequência não está em ordem decrescente!')