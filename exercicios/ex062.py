from time import sleep

print(""" ____                                     /\/|       
|  _ \ _ __ ___   __ _ _ __ ___  ___ ___ |/\/_  ___  
| |_) | '__/ _ \ / _` | '__/ _ \/ __/ __|/ _` |/ _ \ 
|  __/| | | (_) | (_| | | |  __/\__ \__ \ (_| | (_) |
|_| _ |_|  \___/_\__, |_|  \___||___/___/\__,_|\___/ 
   / \   _ __(_) |___/__ ___   /_/| |_(_) ___ __ _   
  / _ \ | '__| | __| '_ ` _ \ / _ \ __| |/ __/ _` |  
 / ___ \| |  | | |_| | | | | |  __/ |_| | (_| (_| |  
/_/   \_\_|  |_|\__|_| |_| |_|\___|\__|_|\___\__,_|  """)

termo = int(input("\nQual o 1° TERMO da sua PA? "))
razao = int(input("Qual a RAZÃO da sua PA? "))
inicio = 1
termos = 10
condicao = True
quantidadeDeTermosTotal = 0

print("\n10 PRIMEIROS TERMOS DA PA:")
while inicio <= termos:
    print(termo, "→ ", end="")
    termo += razao
    inicio += 1
print("FIM!")

while condicao:
    inicio = 1
    quantidadeDeTermos = int(input("Deseja ver mais termos?\nInforme a quantidade ou 0 para sair: "))
    quantidadeDeTermosTotal += quantidadeDeTermos
    if quantidadeDeTermos == 0:
        print("\nProgressão finalizada com {} termos mostrados.".format(termos + quantidadeDeTermosTotal))
        print("\nFinalizando programa...")
        sleep(3)
        print("Programa finalizado!")
        condicao = False
    elif quantidadeDeTermos < 0:
        print("\nTermo inválido!")
    else:
        while inicio <= quantidadeDeTermos:
            print(termo, "→ ", end="")
            termo += razao
            inicio += 1
        print("PAUSA")
