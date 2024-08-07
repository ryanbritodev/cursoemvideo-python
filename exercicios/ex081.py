print("""    _            __  _ _                _      
   / \   _ __   /_/_| (_)___  ___    __| | ___ 
  / _ \ | '_ \ / _` | | / __|/ _ \  / _` |/ _ |
 / ___ \| | | | (_| | | \__ \  __/ | (_| |  __/
/_/   \_\_| |_|\__,_|_|_|___/\___|  \__,_|\___|
 _   _ _ __ ___   __ _  | |   (_)___| |_ __ _  
| | | | '_ ` _ \ / _` | | |   | / __| __/ _` | 
| |_| | | | | | | (_| | | |___| \__ \ || (_| | 
 \__,_|_| |_| |_|\__,_| |_____|_|___/\__\__,_| \n""")

valores = list()
cont = 1

while True:
    valores.append(int(input(f"Digite o {cont}° valor: ")))
    cont += 1
    flag = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if flag == "N":
        break
    while flag not in "SN":
        flag = str(input("Deseja continuar? [S/N] ")).strip().upper()

valores.sort(reverse=True)

print(f"\nQuantidade de números que foram digitados: {len(valores)}")
print(f"Lista de valores em ordem decrescente: {valores}")

if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista!")
