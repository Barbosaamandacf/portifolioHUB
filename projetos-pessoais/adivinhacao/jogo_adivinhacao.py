import random

numero_secreto = random.randint(1, 10)

print("JOGO DE ADIVINHAÇÃO")
print("Estou pensando em um número de 1 a 10...")

while True:
    palpite = int(input("Qual é o seu palpite? "))

    if palpite == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR.")
    else:
        print("O número secreto é MENOR.")
