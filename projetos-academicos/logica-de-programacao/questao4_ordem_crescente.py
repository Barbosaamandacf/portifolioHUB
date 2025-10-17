# Questão 4: Ordem crescente de dois valores inteiros
# Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente.

a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))

if a < b:
    print("ordem crescente:", a, b)
else:
    print("ordem crescente:", b, a)