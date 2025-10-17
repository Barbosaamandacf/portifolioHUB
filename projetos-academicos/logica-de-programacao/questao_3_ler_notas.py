# Programa: ler notas

total_alunos = 0
aprovados = 0
reprovados = 0
soma_notas = 0

while True:
    nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))

    if nota == -1:  # condição de parada
        break

    total_alunos += 1
    soma_notas += nota

    if nota >= 5:
        aprovados += 1
    else:
        reprovados += 1

# calcula a média da turma
if total_alunos > 0:
    media = soma_notas / total_alunos
else:
    media = 0

print("Quantidade de alunos:", total_alunos)
print("Quantidade de aprovados:", aprovados)
print("Quantidade de reprovados:", reprovados)
print(f"Média da turma: {media:.2f}")

