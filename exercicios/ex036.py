from time import sleep

cores = {"limpa": "\033[m",
         "negrito": "\033[1m",
         "vermelho": "\033[31m",
         "amarelo": "\033[33m",
         "pretoebranco": "\033[30;107m",
         "amareloenegrito": "\033[1;33m",
         "verdeenegrito": "\033[1;32m",
         "vermelhoenegrito": "\033[1;31m"}

print("""{}                   
                            __      _   _                 
  ___ _ __ ___  _ __  _ __ /_/  ___| |_(_)_ __ ___   ___  
 / _ \ '_ ` _ \| '_ \| '__/ _ \/ __| __| | '_ ` _ \ / _ \ 
|  __/ | | | | | |_) | | |  __/\__ \ |_| | | | | | | (_) |
 \___|_| |_| |_| .__/|_|  \___||___/\__|_|_| |_| |_|\___/ 
               |_|{}""".format(cores["negrito"], cores["limpa"]))
print("""{}                          ⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢯⠙⠩⠀⡇⠊⠽⢖⠆⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠱⣠⠀⢁⣄⠔⠁⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢀⡔⠙⠈⢱⡟⣧⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⡠⠊⠀⠀⣀⡀⠀⠘⠕⢄⠀⠀⠀⠀⠀
                ⠀⠀⠀⢀⠞⠀⠀⢀⣠⣿⣧⣀⠀⠀⢄⠱⡀⠀⠀⠀
                ⠀⠀⡰⠃⠀⠀⢠⣿⠿⣿⡟⢿⣷⡄⠀⠑⢜⢆⠀⠀
                ⠀⢰⠁⠀⠀⠀⠸⣿⣦⣿⡇⠀⠛⠋⠀⠨⡐⢍⢆⠀
                ⠀⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⡀⠀⢀⠨⡒⠙⡄
                ⢠⠁⡀⠀⠀⠀⣤⡀⠀⣿⡇⢈⣿⡷⠀⠠⢕⠢⠁⡇
                ⠸⠀⡕⠀⠀⠀⢻⣿⣶⣿⣷⣾⡿⠁⠀⠨⣐⠨⢀⠃
                ⠀⠣⣩⠘⠀⠀⠀⠈⠙⣿⡏⠁⠀⢀⠠⢁⡂⢉⠎⠀
                ⠀⠀⠈⠓⠬⢀⣀⠀⠀⠈⠀⠀⠀⢐⣬⠴⠒⠁⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉{}""".format(cores["negrito"], cores["limpa"]))
valorCasa = float(input("\n{}INFORME O VALOR DA CASA:{} {}R${}".format(cores["negrito"], cores["limpa"], cores["verdeenegrito"], cores["limpa"])))
salario = float(input("{}INFORME O SEU SALÁRIO:{} {}R${}".format(cores["negrito"], cores["limpa"], cores["verdeenegrito"], cores["limpa"])))
meses = float(input("{}INFORME A QUANTIDADE DE PRESTAÇÕES MENSAIS:{} ".format(cores["negrito"], cores["limpa"])))

prestacao = valorCasa / meses

print("{}PROCESSANDO...{}".format(cores["amareloenegrito"], cores["limpa"]))
sleep(5)

if prestacao > (salario * 0.3):
    print("{}Infelizmente, você NÃO pode financiar essa casa!{}".format(cores["vermelhoenegrito"], cores["limpa"]))
else:
    print("{}Parabéns! Você PODE financiar essa casa!{}".format(cores["verdeenegrito"], cores["limpa"]))

print("{}VALOR FINAL DAS PRESTAÇÕES:{} {}R${:.2f}{}".format(cores["negrito"], cores["limpa"], cores["verdeenegrito"], prestacao, cores["limpa"]))
