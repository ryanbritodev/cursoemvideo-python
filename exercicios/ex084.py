dado = []
pessoas = []
maiorPeso = 0
while True:
    dado.append(str(input("Nome: ")).strip().title())
    dado.append(float(input("Peso: ")))
    pessoas.append(dado.copy())
    dado.clear()
    flag = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while flag not in "SN":
        print("Opção inválida!")
        flag = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if flag == "N":
        break
    else:
        continue
print("-=" * 30)

menorPeso = pessoas[0][1]
pessoasMenor = []
pessoasMaior = []

# for p in pessoas:
#   if p[1] == maiorPeso:
#       print(f"[{p[0]}] ", end="")

for pessoa in pessoas:
    if pessoa[1] > maiorPeso:
        maiorPeso = pessoa[1]
    if pessoa[1] < menorPeso:
        menorPeso = pessoa[1]

for pessoa in pessoas:
    if pessoa[1] == maiorPeso:
        pessoasMaior.append(pessoa[0])
    if pessoa[1] == menorPeso:
        pessoasMenor.append(pessoa[0])

print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maiorPeso}Kg. Peso de ", end="")
for c in pessoasMaior:
    print(c, end=" ")
print(f"\nO menor peso foi de {menorPeso}Kg. Peso de ", end="")
for c in pessoasMenor:
    print(c, end=" ")
