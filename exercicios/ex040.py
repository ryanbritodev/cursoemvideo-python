print("""{} __  __   __  ____ ___    _      _____ ___ _   _    _    _     
|  \/  |_/_/_|  _ \_ _|  / \    |  ___|_ _| \ | |  / \  | |    
| |\/| | ____| | | | |  / _ \   | |_   | ||  \| | / _ \ | |    
| |  | |  _|_| |_| | | / ___ \  |  _|  | || |\  |/ ___ \| |___ 
|_|  |_|_____|____/___/_/   \_\ |_|   |___|_| \_/_/   \_\_____|
{}""".format("\033[1m", "\033[m"))

nota1 = float(input("{}NOTA DA 1° PROVA{}: ".format("\033[1m", "\033[m")))
nota2 = float(input("{}NOTA DA 2° PROVA{}: ".format("\033[1m", "\033[m")))

media = (nota1 + nota2) / 2

if media < 5:
    print("Você está {}REPROVADO{}!".format("\033[1;31m", "\033[m"))
elif 5 <= media <= 6.9:
    print("Você está de {}RECUPERAÇÃO{}!".format("\033[1;33m", "\033[m"))
else:
    print("Você foi {}APROVADO{}! Parabéns!".format("\033[1;32m", "\033[m"))
