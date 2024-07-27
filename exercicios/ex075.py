print(""" _____            _             _         
|_   _|   _ _ __ | | __ _    __| | ___    
  | || | | | '_ \| |/ _` |  / _` |/ _ \   
  | || |_| | |_) | | (_| | | (_| |  __/   
  |_| \__,_| .__/|_|\__,_|  \__,_|\___|   
 _   _   __|_|                            
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___ 
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|
| |\  | |_| | | | | | |  __/ | | (_) \__ |
|_| \_|\__,_|_| |_| |_|\___|_|  \___/|___/""")

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
valor4 = int(input("Digite o quarto valor: "))
valor5 = int(input("Digite o quinto valor: "))

tuplaNum = (valor1, valor2, valor3, valor4, valor5)
print(f"Você digitou os valores {tuplaNum}")

cont9 = 0
temTres = temPar = False

for c in range(0, 5):
    if tuplaNum[c] == 9:
        cont9 += 1
    else:
        continue

print(f"O valor 9 apareceu {cont9} vezes")

for p in range(0, 5):
    if tuplaNum[p] == 3:
        temTres = True
        break

if temTres:
    if tuplaNum.index(3) == 0:
        print("O valor 3 foi digitado pela primeira vez no índice 0")
    else:
        print(f"O valor 3 foi digitado pela primeira vez no {tuplaNum.index(3)}° índice", end="")

if not temTres:
    print("O valor 3 não foi digitado em nenhuma posição")

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
