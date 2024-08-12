print(""" _     _     _          ___        __ _       _ _        
| |   (_)___| |_ __ _  |_ _|_ __  / _(_)_ __ (_) |_ __ _ 
| |   | / __| __/ _` |  | || '_ \| |_| | '_ \| | __/ _` |
| |___| \__ \ || (_| |  | || | | |  _| | | | | | || (_| |
|_____|_|___/\__\__,_| |___|_| |_|_| |_|_| |_|_|\__\__,_|""")

print("""     
     ⣀⣤⣴⣶⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣦⣤⡀⠀⠀⠀⠀
⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
⠀⠀⣾⣿⠟⠋⠉⠀⠀⠉⠙⠻⣿⣷⡀⣰⣿⣿⣿⠟⠉⠀⠀⠀⠈⠙⣿⣷⠀⠀
⠀⢸⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀  ⠸⣿⡇⠀
⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀  ⠀ ⣿⡇⠀
⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀  ⢰⣿⡇⠀
⠀⠀⢿⣿⣄⡀⠀⠀⠀⢀⣴⣿⣿⣿⠟⠘⢿⣿⣦⣀⡀⠀⠀ ⢀⣴⣿⡿⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⠿⠿⠛⠉\n""")

cont = 0
valores = []

while True:
    cont += 1
    valor = int(input(f"Digite o {cont}° valor: "))
    if valor in valores:
        print("Valor duplicado! Não vou adicionar...")
    if valor not in valores:
        valores.append(valor)
        print("Valor adicionado com sucesso...")
    flag = str(input("Quer continuar? [S/N] ")).strip().upper()
    if flag == "S":
        continue
    elif flag == "N":
        break
    else:
        while flag != "N" or flag != "S":
            flag = str(input("Quer continuar? [S/N] ")).strip().upper()
            if flag == "N" or flag == "S":
                break

valores.sort()

<<<<<<< HEAD
print(f"\nVocê digitou os valores {valores}")
=======
print("=-" * 30)
print(f"Você digitou os valores {valores}")
>>>>>>> 6b2aef8e10357f4ff86d2471dfe01288fb0cf736
