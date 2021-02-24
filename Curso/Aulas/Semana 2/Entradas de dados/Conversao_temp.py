# Programinha simples para converter temperatura ºF em ºC

tempF = float(input('Qual o valor da temperatura em F? '))
tempC = ((tempF - 32) * 5) / 9

print('A temperatura em Celsius é {:.2f}ºC'.format(tempC))