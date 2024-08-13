estado = dict()
brasil = list()
for dados in range(0, 3):
    estado["UF"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
print(brasil)

for estado in brasil:
    for chave, valor in estado.items():
        print(f"O campo {chave} tem valor {valor}.")
