print(""" _   _   __                               
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___ 
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|
| |\  | |_| | | | | | |  __/ | | (_) \__ |
|_|_\_|\__,_|_| |_|_|_|\___|_|  \___/|___/
|_ _|_ __ | |_ ___(_)_ __ ___  ___        
 | || '_ \| __/ _ \ | '__/ _ \/ __|       
 | || | | | ||  __/ | | | (_) \__ \       
|___|_| |_|\__\___|_|_|  \___/|___/       """)

condicao = True
contador = 0
soma = 0
listaNum = list()

while condicao:
    num = int(input("\nDigite um número inteiro\n(ou [0] para parar de ler): "))
    listaNum.append(num)
    contador += 1
    soma += num
    if num == 0:
        ultimoItem = listaNum.pop()
        print("\nMédia dos Números: {:.2f}\nMaior número: {}\nMenor número: {}\n".format(soma / (contador - 1), max(listaNum), min(listaNum)))
        decisao = str(input("Deseja continuar? [S/N] ")).strip().lower().replace(" ", "")
        if decisao == "s":
            continue
        else:
            print("\nObrigado! Até mais :)")
            condicao = False
