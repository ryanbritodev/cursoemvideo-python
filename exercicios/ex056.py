from numpy import array

print(""" ____  _____ ____ ____   ___    _    ____  
|  _ \| ____/ ___/ ___| / _ \  / \  / ___| 
| |_) |  _| \___ \___ \| | | |/ _ \ \___ \ 
|  __/| |___ ___) |__) | |_| / ___ \ ___) |
|_|   |_____|____/____/ \___/_/   \_\____/ \n""")

listaNomeMasculino = []
listaIdadeMasculina = []
listaSexoMasculino = []
listaNomeFeminino = []
listaIdadeFeminina = []
listaSexoFeminino = []

for i in range(1, 5):
    nome = str(input("Qual seu nome? ")).strip().lower().title()
    idade = int(input("{}, qual sua idade? ".format(nome)))
    sexo = str(input("{}, qual é o seu gênero? Masculino ou Feminino? ".format(nome))).strip().lower()
    print("Muito obrigado pelas informações, {}!\n".format(nome))
    if sexo == "masculino":
        listaNomeMasculino.append(nome)
        listaIdadeMasculina.append(idade)
        listaSexoMasculino.append(sexo)
    elif sexo == "feminino":
        listaIdadeFeminina.append(idade)
        listaNomeFeminino.append(nome)
        listaSexoFeminino.append(sexo)

mediaIdades = (sum(listaIdadeMasculina) + sum(listaIdadeFeminina)) / 4

print("A média das idades de todas as pessoas é de {:.1f} anos".format(mediaIdades))

if not listaNomeMasculino:
    print("Não existe nenhum homem entre todas as pessoas!")
else:
    idadeHomemMaisVelho = max(listaIdadeMasculina)
    homemMaisVelho = listaNomeMasculino[array(listaIdadeMasculina).argmax()]
    print("O homem mais velho entre todas as pessoas é {}, com {} anos".format(homemMaisVelho, idadeHomemMaisVelho))

quantidadeMulheres = 0

for idade in listaIdadeFeminina:
    if idade < 20:
        quantidadeMulheres += 1

if not listaIdadeFeminina:
    print("Não existe nenhuma mulher entre todas as pessoas!")
elif quantidadeMulheres == 0:
    print("Não existe nenhuma mulher com menos de 20 anos entre as pessoas!")
else:
    print("A quantidade de mulheres que tem menos de 20 anos é de {} mulheres".format(quantidadeMulheres))
