aluno = {}

situacao = ""

nome = str((input("Nome: ")).strip().title())
aluno["nome"] = nome

media = float(input(f"Média de {nome}: "))
aluno["média"] = media

if aluno["média"] > 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

aluno["situação"] = situacao

print(f"Nome é igual a {aluno["nome"]}")
print(f"Média é igual a {aluno["média"]}")
print("Situação é igual a Aprovado" if aluno["situação"] == "Aprovado" else "Situação é igual a Reprovado")
