print(""" _   _   __                           
| \ | |_/_/_ _ __ ___   ___ _ __ ___  
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \ 
| |\  | |_| | | | | | |  __/ | | (_) |
|_|_\_|\__,_|_| |_| |_|\___|_|  \___/ 
| ____|_  _| |_ ___ _ __  ___  ___    
|  _| \ \/ / __/ _ \ '_ \/ __|/ _ \   
| |___ >  <| ||  __/ | | \__ \ (_) |  
|_____/_/\_\\__\___|_| |_|___/\___/   """)

contagem = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

num = int(input("Digite um número entre 0 a 20: "))

while num < 0 or num > 20:
    print("Tente novamente!")
    num = int(input("Digite um número de 0 a 20: "))

print(f"O número que você digitou é o {contagem[num]}!")
