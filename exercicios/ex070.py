print(""" __  __                        _ _       _           
|  \/  | ___ _ __ ___ __ _  __| (_)_ __ | |__   ___  
| |\/| |/ _ \ '__/ __/ _` |/ _` | | '_ \| '_ \ / _ \ 
| |  | |  __/ | | (_| (_| | (_| | | | | | | | | (_) |
|_|__|_|\___|_|  \___\__,_|\__,_|_|_| |_|_| |_|\___/ 
| __ )(_) __ _  | __ )  ___  _ __ ___    _____|  _ \ 
|  _ \| |/ _` | |  _ \ / _ \| '_ ` _ \  |_____| | | |
| |_) | | (_| | | |_) | (_) | | | | | | |_____| |_| |
|____/|_|\__, | |____/ \___/|_| |_| |_|       |____/ 
         |___/                                       \n""")

menor = cont = valor = produto = nomeMenor = soma = contValor = 0

while True:
    produto = str(input("Nome do produto: ").strip())
    valor = float(input("Preço: R$"))
    while valor < 1:
        print("Valor inválido! Digite novamente")
        valor = float(input("Preço: R$"))
    cont += 1
    if cont == 1:
        menor = valor
        nomeMenor = produto
    else:
        if valor < menor:
            menor = valor
            nomeMenor = produto
    soma += valor
    if valor > 1000:
        contValor += 1
    flag = str(input("Quer continuar? [S/N] ").replace(" ", "").upper())
    while flag != "S" and flag != "N":
        flag = str(input("Quer continuar? [S/N] ").replace(" ", "").upper())
    if flag == "N":
        print("{:-^50}".format(" PROGRAMA ENCERRADO "))
        break
    else:
        continue
print(f"O total da compra foi R${soma:.2f}")
print(f"Temos {contValor} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nomeMenor}, com o valor de R${menor}")
