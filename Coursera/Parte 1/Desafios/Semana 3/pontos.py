# Programa para medir se a distância entre dois pontos é perto ou longe

import math
x1 = float(input('Digite a coordenada X do primeiro ponto: '))
y1 = float(input('Digite a coordenada Y do primeiro ponto: '))
x2 = float(input('Digite a coordenada X do segundo ponto: '))
y2 = float(input('Digite a coordenada Y do segundo ponto: '))

# Formula para calcular a distância num plano cartesiano
# d(x,y) = √/ (x1-x2)² + (y1-y2)²
distancia = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))

if distancia >= 10:
    print('longe')

else:
    print('perto')
