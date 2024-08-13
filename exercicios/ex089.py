from time import sleep

alunos = []

while True:
    nome = str(input("Nome: ")).strip().title()
    nota = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    alunos.append([nome, nota, nota2])
    flag = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while flag != "S" and flag != "N":
        print("Opcção inválida!")
        flag = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if flag == "S":
        continue
    else:
        break

quantidadeIndice = []

print("-=" * 30)
print("N° NOME              MÉDIA")
print("--------------------------")
for indice, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f"{indice:<2} {aluno[0]:<15} {media:>7.2f}")
    quantidadeIndice.append(indice)
print("--------------------------")

while True:
    mostrarNota = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    while mostrarNota not in quantidadeIndice:
        if mostrarNota == 999:
            break
        else:
            print("Aluno não encontrado!")
            mostrarNota = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if mostrarNota != 999:
        print(f"Notas de {alunos[mostrarNota][0]} são {alunos[mostrarNota][1:]}")
    if mostrarNota == 999:
        break
print("FINALIZANDO...")
sleep(1)
print("<<< VOLTE SEMPRE >>>")
