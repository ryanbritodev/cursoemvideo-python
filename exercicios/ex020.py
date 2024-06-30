from random import shuffle

aluno1 = input("Aluno 1, digite seu nome: ")
aluno2 = input("Aluno 2, digite seu nome: ")
aluno3 = input("Aluno 3, digite seu nome: ")
aluno4 = input("Aluno 4, digite seu nome: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)

ordemAlunos = ", ".join(alunos)

print("A ordem de apresentação será assim:\n{}".format(ordemAlunos))
