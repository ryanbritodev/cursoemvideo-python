print(""" ____   ___  __  __    _       
/ ___| / _ \|  \/  |  / \      
\___ \| | | | |\/| | / _ \     
 ___) | |_| | |  | |/ ___ \    
|____/ \___/|_|__|_/_/__ \_\_  
|  _ \ / \  |  _ \| ____/ ___| 
| |_) / _ \ | |_) |  _| \___ \ 
|  __/ ___ \|  _ <| |___ ___) |
|_| /_/   \_\_| \_\_____|____/ \n""")

soma = 0
somaZero = 0
cont = 0

# shift + tab = voltar identação do bloco

for i in range(1, 7):
    num = int(input("INFORME O {}° NÚMERO INTEIRO: ".format(i)))
    if num % 2 == 0 and num != 0:
        soma += num
        cont += 1
    if num == 0:
        somaZero += 1

if somaZero == 6:
    print("\nTodos os NÚMEROS informados foram 0!")
elif soma == 0 and somaZero >= 1:
    print("\nNenhum NÚMERO PAR foi informado (além de 0)!")
elif soma == 0:
    print("\nNenhum NÚMERO PAR foi informado!")
else:
    print("\nSOMATÓRIO DOS {} NÚMEROS PARES: {}".format(cont, soma))
