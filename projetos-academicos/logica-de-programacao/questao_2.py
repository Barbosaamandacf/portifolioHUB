# O que o programa deve fazer:

#O usuário digita vários valores reais (números com vírgula).

#No final, o programa mostra:

###Quantidade de valores digitados;

#Média aritmética;

#Quantos valores foram maiores que 20.

# Programa: leitura de vários valores reais

contador = 0        # conta quantos valores foram digitados
soma = 0            # soma todos os valores
maiores20 = 0       # conta quantos valores são > 20

while True:
    valor = float(input("Digite um valor real (ou 0 para parar): "))

    if valor == 0:   # condição de parada
        break

    contador += 1
    soma += valor

    if valor > 20:
        maiores20 += 1

# calcula a média (se houver valores digitados)
if contador > 0:
    media = soma / contador
else:
    media = 0

print("Quantidade de valores digitados:", contador)
print("Soma dos valores:", soma)
print("Média aritmética:", media)
print("Quantidade de valores maiores que 20:", maiores20)
