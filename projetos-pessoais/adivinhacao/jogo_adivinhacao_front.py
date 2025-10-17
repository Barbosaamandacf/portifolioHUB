import tkinter as tk
import random

numero_secreto = random.randint(1, 10)

def verificar():
    try:
        palpite = int(entrada.get())
        if palpite == numero_secreto:
            resultado["text"] = "🎉 Acertou!"
        elif palpite < numero_secreto:
            resultado["text"] = "O número é MAIOR"
        else:
            resultado["text"] = "O número é MENOR"
    except:
        resultado["text"] = "Digite um número válido"

janela = tk.Tk()
janela.title("Jogo de Adivinhação")

tk.Label(janela, text="Adivinhe o número de 1 a 10").pack(pady=5)

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Tentar", command=verificar).pack(pady=5)

resultado = tk.Label(janela, text="")
resultado.pack(pady=5)

janela.mainloop()
