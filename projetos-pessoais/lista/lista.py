tarefas = []

while True:
    print("\n LISTA DE TAREFAS")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
    elif opcao == "2":
        print("\nTarefas:")
        if len(tarefas) == 0:
            print("Nenhuma tarefa encontrada.")
        else:
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
    elif opcao == "3":
        print("\nTarefas:")
        for i, t in enumerate(tarefas,1):
            print(f"{i}. {t}")
        num = int(input("Digite o número da tarefa para remover: "))
        if 1 <= num <= len(tarefas):
            tarefas.pop(num-1)
            print("Tarefa removida!")
        else:
            print("Número inválido.")
    elif opcao == "4":
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")