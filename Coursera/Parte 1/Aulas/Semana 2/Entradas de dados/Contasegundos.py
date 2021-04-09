# Programa para converter segundos em dias, horas, minutos e segundos

segundos = int(input('Por gentileza, insira a quantidade de segundos que deseja converter '))

# Primeiro se encontra o valor dos dias e se remove apenas a parte inteira
dias = segundos // 86400
# A parte que resta é separado para em cima desse valor encontrar as horas
dias_seg = segundos % 86400
# Os segundos "restantes" do dia são utilizados para encontrar o valor das horas, e se remove apenas a parte inteira
horas = segundos // 3600
# A parte que resta é separado e esse valor é utilizado na hora de encontrar os minutos
segundos_hora = segundos % 3600
# O valor de segundos que sobraram das horas é convertido em minutos
minutos = segundos_hora // 60
# O valor de segundos que sobraram são mostrados
segun_rest = segundos_hora % 60

print('{} segundos é igual a: {} horas, {} minutos e {} segundos'.format(segundos, horas, minutos, segun_rest))
