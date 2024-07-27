print(""" _____            _             _         
|_   _|   _ _ __ | | __ _    __| | ___    
  | || | | | '_ \| |/ _` |  / _` |/ _ \   
  | || |_| | |_) | | (_| | | (_| |  __/   
  |_| \__,_| .__/|_|\__,_|  \__,_|\___|   
 _   _   __|_|                            
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___ 
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|
| |\  | |_| | | | | | |  __/ | | (_) \__ |
|_| \_|\__,_|_| |_| |_|\___|_|  \___/|___/\n""")

tuplaNum = (int(input("Digite o primeiro valor: ")),
            int(input("Digite o segundo valor: ")),
            int(input("Digite o terceiro valor: ")),
            int(input("Digite o quarto valor: ")),
            int(input("Digite o quinto valor: ")))

print(f"Você digitou os valores {tuplaNum}")

cont9 = 0
temTres = temPar = False

for c in range(0, 5):
    if tuplaNum[c] == 9:
        cont9 += 1
    else:
        continue

if cont9 > 1:
    print(f"O valor 9 apareceu {cont9} vezes")
elif cont9 == 1:
    print("O valor 9 apareceu 1 vez")
if cont9 == 0:
    print("O valor 9 não apareceu nenhuma vez")

for p in range(0, 5):
    if tuplaNum[p] == 3:
        temTres = True
        break

if temTres:
    if tuplaNum.index(3) == 0:
        print("O valor 3 apareceu na 1° posição")
    else:
        print(f"O valor 3 apareceu na {tuplaNum.index(3) + 1}° posição\n", end="")

if not temTres:
    print("O valor 3 não apareceu em nenhuma posição")

if tuplaNum[0] % 2 == 0 or tuplaNum[1] % 2 == 0 or tuplaNum[2] % 2 == 0 or tuplaNum[3] % 2 == 0 or tuplaNum[4] % 2 == 0:
    temPar = True

if temPar:
    print("Os valores pares digitados foram ", end="")
    for i in range(0, 5):
        if tuplaNum[i] % 2 == 0:
            print("{}".format(tuplaNum[i]), end=" ")
        else:
            continue
else:
    print("Nenhum valor par foi informado")
