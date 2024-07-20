print(""" _   _   __                               
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___ 
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|
| |\  | |_| | | | | | |  __/ | | (_) \__ |
|_|_\_|\__,_|_| |_|_|_|\___|_|  \___/|___/
|_ _|_ __ | |_ ___(_)_ __ ___  ___        
 | || '_ \| __/ _ \ | '__/ _ \/ __|       
 | || | | | ||  __/ | | | (_) \__ \       
|___|_| |_|\__\___|_|_|  \___/|___/       \n""")

soma = contador = 0

num = int(input("Digite um número inteiro (ou 999 para parar de ler): "))

while num != 999:
    soma += num
    contador += 1
    num = int(input("Digite um número inteiro (ou 999 para parar de ler): "))
print("\nVocê digitou {} números e a soma entre eles foi {}!".format(contador, soma))
