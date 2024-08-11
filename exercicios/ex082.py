print(""" _   _   __                               
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___ 
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|
| |\  | |_| | | | | | |  __/ | | (_) \__ |
|_| \_|\__,_|_| |_| |_|\___|_|  \___/|___/
 __  __   __  _ _   _       _             
|  \/  |_/_/_| | |_(_)_ __ | | ___  ___   
| |\/| | | | | | __| | '_ \| |/ _ \/ __|  
| |  | | |_| | | |_| | |_) | | (_) \__ \  
|_|  |_|\__,_|_|\__|_| .__/|_|\___/|___/  
                     |_|                  \n""")

lista = []

while True:
    valor = int(input(f"Digite um número: "))
    lista.append(valor)
    flag = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while flag != "S" and flag != "N":
        flag = str(input("Resposta inválida!\nDeseja continuar? [S/N] ")).strip().upper()
    if flag == "N":
        break

listaPares = []
listaImpares = []

for num in range(0, len(lista)):
    if lista[num] % 2 == 0:
        listaPares.append(lista[num])
    else:
        listaImpares.append(lista[num])

print("=-" * 30)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {listaPares}")
print(f"A lista de ímpares é {listaImpares}")
