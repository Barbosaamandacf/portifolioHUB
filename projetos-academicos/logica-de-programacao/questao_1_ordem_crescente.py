# 1.	Elabore o programa que simule a calculadora com as quatro operações aritméticas básicas. O usuário fornecerá dois números e a operação aritmética desejada. Mostre o menu com estes símbolos (+ , - , * , / ) para o usuário escolher a operação aritmética. 
#Utilize o comando “se . . . senão . . . ” encadeado, ou seja, “if . . . else . . . ” encadeado. 

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a < b:
    print("Ordem crescente:", a, b)
else:
    print("Ordem crescente:", b, a)
