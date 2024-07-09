from time import sleep

cores = {"limpa": "\033[m",
         "negrito": "\033[1m",
         "vermelho": "\033[31m",
         "amarelo": "\033[33m",
         "pretoebranco": "\033[30;107m",
         "amareloenegrito": "\033[1;33m",
         "verdeenegrito": "\033[1;32m",
         "vermelhoenegrito": "\033[1;31m"}

print("{}={}".format(cores["negrito"], cores["limpa"])*72)
print("""{}  ___  _   _   _    _         __    __  __    _    ___ ___  ____    ___ 
 / _ \| | | | / \  | |      _/_/_  |  \/  |  / \  |_ _/ _ \|  _ \  |__ |
| | | | | | |/ _ \ | |     | ____| | |\/| | / _ \  | | | | | |_) |   / /
| |_| | |_| / ___ \| |___  |  _|_  | |  | |/ ___ \ | | |_| |  _ <   |_| 
 \__\_|\___/_/   \_\_____| |_____| |_|  |_/_/   \_\___\___/|_| \_\  (_) 
{}""".format(cores["negrito"], cores["limpa"]))
print("{}={}".format(cores["negrito"], cores["limpa"])*72)

num1 = int(input("\n{}Informe o 1° NÚMERO inteiro: {}".format(cores["negrito"], cores["limpa"])))
num2 = int(input("{}Informe o 2° NÚMERO inteiro: {}".format("\033[1m", "\033[m")))

if num1 > num2:
    print("\n{}PROCESSANDO...{}".format("\033[1;33m", "\033[m"))
    sleep(1.5)
    print("\n{}O número {} é MAIOR do que o número {}!{}".format(cores["negrito"], num1, num2, cores["limpa"]))
elif num2 > num1:
    print("\n{}PROCESSANDO...{}".format(cores["amareloenegrito"], cores["limpa"]))
    sleep(1.5)
    print("\n{}O número {} é MAIOR do que o número {}!{}".format(cores["negrito"], num2, num1, cores["limpa"]))
elif num1 == num2:
    print("\n{}PROCESSANDO{}...".format(cores["amareloenegrito"], cores["limpa"]))
    sleep(1.5)
    print("\n{}Não existe valor maior, os dois números são IGUAIS!{}".format(cores["negrito"], cores["limpa"]))
else:
    print("\n{}Número inválido!{}".format(cores["vermelhoenegrito"], cores["limpa"]))
