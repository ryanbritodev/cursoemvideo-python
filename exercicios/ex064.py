print(""" _   _   __                               
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___ 
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|
| |\  | |_| | | | | | |  __/ | | (_) \__ |
|_|_\_|\__,_|_| |_|_|_|\___|_|  \___/|___/
|_ _|_ __ | |_ ___(_)_ __ ___  ___        
 | || '_ \| __/ _ \ | '__/ _ \/ __|       
 | || | | | ||  __/ | | | (_) \__ \       
|___|_| |_|\__\___|_|_|  \___/|___/       \n""")

condicao = True
soma = 0
contador = 0

while condicao:
    num = int(input("Digite um número inteiro (ou 999 para parar de ler): "))
    soma += num
    contador += 1
    if num == 999:
        print("\nEncerrando as leituras...\n")
        print("Soma entres os números: {}\nQuantidade de números digitados: {}".format(soma - 999, contador - 1))
        condicao = False
