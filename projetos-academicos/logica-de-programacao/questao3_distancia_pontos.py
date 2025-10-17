# Questão 3: Distância entre dois pontos
# Construa o programa que calcule a distância entre dois pontos P(x1, y1) e Q(x2, y2).
# Fórmula: distância = sqrt((x2 - x1)^2 + (y2 - y1)^2)

import math  # para usar sqrt

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))


distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("A distância entre os pontos é:", distancia)

