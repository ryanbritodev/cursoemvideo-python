print(""" _   _   __                               
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___ 
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|
| |\  | |_| | | | | | |  __/ | | (_) \__ |
|_|_\_|\__,_|_| |_|_|_|\___|_|  \___/|___/
|_ _|_ __ | |_ ___(_)_ __ ___  ___        
 | || '_ \| __/ _ \ | '__/ _ \/ __|       
 | || | | | ||  __/ | | | (_) \__ \       
|___|_| |_|\__\___|_|_|  \___/|___/       \n""")

contador = soma = 0

while True:
    num = int(input("Digite um número inteiro [ou 999 para sair]: "))
    if num == 999:
        break
    contador += 1
    soma += num
print(f"\nA soma entre os {contador} números vale {soma}!")
