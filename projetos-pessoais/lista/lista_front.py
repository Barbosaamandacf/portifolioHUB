import tkinter as tk

def adicionar():
    tarefa = entrada.get()
    if tarefa:
        lista.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)

def remover():
    selecionado = lista.curselection()
    if selecionado:
        lista.delete(selecionado)

janela = tk.Tk()
janela.title("Lista de Tarefas")

entrada = tk.Entry(janela, width=40)
entrada.pack(pady=5)

btn_adicionar = tk.Button(janela, text="Adicionar", command=adicionar)
btn_adicionar.pack()

btn_remover = tk.Button(janela, text="Remover", command=remover)
btn_remover.pack()

lista = tk.Listbox(janela, width=40, height=10)
lista.pack(pady=5)

janela.mainloop()
