import tkinter as tk

def calcular(operacao):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())

        if operacao == "somar":
            resultado["text"] = f"Resultado: {n1 + n2}"
        elif operacao == "subtrair":
            resultado["text"] = f"Resultado: {n1 - n2}"
        elif operacao == "multiplicar":
            resultado["text"] = f"Resultado: {n1 * n2}"
        elif operacao == "dividir":
            if n2 != 0:
                resultado["text"] = f"Resultado: {n1 / n2}"
            else:
                resultado["text"] = "Erro: divisão por zero"
    except:
        resultado["text"] = "Erro: insira números válidos"

janela = tk.Tk()
janela.title("Calculadora")

tk.Label(janela, text="Número 1:").pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Número 2:").pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

tk.Button(janela, text="Somar", command=lambda: calcular("somar")).pack()
tk.Button(janela, text="Subtrair", command=lambda: calcular("subtrair")).pack()
tk.Button(janela, text="Multiplicar", command=lambda: calcular("multiplicar")).pack()
tk.Button(janela, text="Dividir", command=lambda: calcular("dividir")).pack()

resultado = tk.Label(janela, text="Resultado: ")
resultado.pack(pady=10)

janela.mainloop()
