galera = []
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

print(galera)

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é maior de idade.")
        totmaior += 1
    else:
        print(f"{pessoa[0]} é menor de idade.")
        totmenor += 1

print(f"Temos {totmaior} maiores e {totmenor} menores de idade.")

# Explicação:
# Criamos uma lista chamada galera
# Criamos uma lista chamada dado
# Criamos um loop que vai de 0 a 3
# Adicionamos o nome na lista dado
# Adicionamos a idade na lista dado
# Adicionamos a lista dado na lista galera
# Limpamos a lista dado
