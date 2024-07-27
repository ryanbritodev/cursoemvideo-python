import sys

print(""" _   _   __                           
| \ | |_/_/_ _ __ ___   ___ _ __ ___  
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \ 
| |\  | |_| | | | | | |  __/ | | (_) |
|_|_\_|\__,_|_| |_| |_|\___|_|  \___/ 
| ____|_  _| |_ ___ _ __  ___  ___    
|  _| \ \/ / __/ _ \ '_ \/ __|/ _ \   
| |___ >  <| ||  __/ | | \__ \ (_) |  
|_____/_/\_||__\___|_| |_|___/\___/   \n""")

contagem = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
            "Seis", "Sete", "Oito", "Nove", "Dez", "Onze",
            "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis",
            "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input("Digite um número de 0 a 20: "))
    if 0 <= num <= 20:
        print(f"O número que você digitou é o {contagem[num]}")
        while True:
            flag = str(input("Deseja continuar? [S/N] ")).strip().upper()
            if flag == "S":
                break
            elif flag == "N":
                print("\nEncerrando programa... \nAté mais!")
                sys.exit()
            else:
                print("Opção inválida!")
                continue
