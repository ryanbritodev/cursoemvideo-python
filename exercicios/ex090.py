aluno = dict()
aluno["nome"] = str(input("Nome: ")).strip().title()
aluno["media"] = float(input(f"Média de {aluno["nome"]}: "))
if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
elif 5 <= aluno["media"] < 7:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"
print("-=" * 30)
for k, v in aluno.items():
    print(f"    - {k} é igual {v}") # Keys e Valores sendo percorridos

# aluno = {}
#
# situacao = ""
#
# nome = str((input("Nome: ")).strip().title())
# aluno["nome"] = nome
#
# media = float(input(f"Média de {nome}: "))
# aluno["média"] = media
#
# if aluno["média"] > 6:
#     situacao = "Aprovado"
# else:
#     situacao = "Reprovado"
#
# aluno["situação"] = situacao
#
# print(f"Nome é igual a {aluno["nome"]}")
# print(f"Média é igual a {aluno["média"]}")
# print("Situação é igual a Aprovado" if aluno["situação"] == "Aprovado" else "Situação é igual a Reprovado")
