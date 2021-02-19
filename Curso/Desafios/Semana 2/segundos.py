segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = segundos // 86400
dias_seg = segundos % 86400
horas = dias_seg // 3600
horas_seg = dias_seg % 3600
minutos = horas_seg // 60
minutos_seg = dias_seg % 60

print(dias,'dias,',horas,'horas,',minutos,'minutos e',minutos_seg,'segundos.')