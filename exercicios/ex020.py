import random

aluno1 = input("Aluno 1, digite seu nome: ")
aluno2 = input("Aluno 2, digite seu nome: ")
aluno3 = input("Aluno 3, digite seu nome: ")
aluno4 = input("Aluno 4, digite seu nome: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)

alunosForaDaLista = map(str, alunos)
ordemAlunos = ", ".join(alunosForaDaLista)

print("A ordem de apresentação será assim: {}".format(ordemAlunos))
