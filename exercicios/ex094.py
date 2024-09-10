pessoas = []
somaIdades = 0

while True:
    nome = str(input("Nome: ")).strip().title()
    while True:
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if sexo != "M" and sexo != "F":
            print("Opção inválida! Digite novamente.")
            continue
        else:
            break
    idade = int(input("Idade: "))
    somaIdades += idade
    while True:
        flag = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if flag != "S" and flag != "N":
            print("Opção inválida! Tente novamente.")
        else:
            break
    pessoa = {"nome": nome, "sexo": sexo, "idade": idade}
    pessoas.append(pessoa)
    if flag == "N":
        break

listaMulheres = []

for i in pessoas:
    if i["sexo"] == "F":
        listaMulheres.append(i["nome"])
    else:
        continue

mediaIdade = somaIdades / len(pessoas)

print("-=" * 35)
print(f"- O grupo tem {len(pessoas)} pessoas.")
print("- A média de idade é de {:.2f} anos.".format(mediaIdade))
print("- As mulheres cadastradas foram: ", end="")
for mulher in listaMulheres:
    print(mulher, end=" ")
print("\n- Lista das pessoas que estão acima da média: \n")

for c in pessoas:
    if c["idade"] > mediaIdade:
        print(f"nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]};")
    else:
        continue

print("\n<< ENCERRADO >>")
