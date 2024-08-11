print(""" _____                               /\/|       
| ____|_  ___ __  _ __ ___  ___ ___ |/\/_  ___  
|  _| \ \/ / '_ \| '__/ _ \/ __/ __|/ _` |/ _ \ 
| |___ >  <| |_) | | |  __/\__ \__ \ (_| | (_) |
|_____/_/\_\ .__/|_|  \___||___/___/\__,_|\___/ 
           |_|                                  \n""")

expressao = str(input("Digite a expressão: "))
listaParenteses = []

for indice in range(0, len(expressao)):
    if expressao[indice] == "(" or expressao[indice] == ")":
        listaParenteses.append(expressao[indice])
    else:
        continue

if listaParenteses.count("(") == listaParenteses.count(")"):
    print("Sua expressão está com a ordem de parênteses CORRETA!")
else:
    print("Sua expressão está com a ordem de parênteses ERRADA!")
