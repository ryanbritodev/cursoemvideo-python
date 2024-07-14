print(""" _   _   __                               
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___ 
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|
| |\  | |_| | | | | | |  __/ | | (_) \__ |
|_|_\_|\__,_|_| |_| |_|\___|_|  \___/|___/
|  _ \ _ __(_)_ __ ___   ___  ___         
| |_) | '__| | '_ ` _ \ / _ \/ __|        
|  __/| |  | | | | | | | (_) \__ \        
|_|   |_|  |_|_| |_| |_|\___/|___/        """)

num = int(input("\n{}Digite um número: {}".format("\033[1m", "\033[m")))
tot = 0

print("")

for i in range(1, num + 1):
    if num % i == 0:
        print("\033[1;32m", end="")
        tot += 1
    else:
        print("\033[1;31m", end="")
    print("{} ".format(i), end="")
print("\n\n\033[m{}O número {} foi divisível {} vezes{}".format("\033[1m", num, tot, "\033[m"))
if tot == 2:
    print("{}E por isso, ele É PRIMO!{}".format("\033[1;32m", "\033[m"))
else:
    print("{}E por isso, ele NÃO É PRIMO!{}".format("\033[1;31m", "\033[m"))

# Solução que eu cheguei ↓

"""num = int(input("\nDigite um NÚMERO INTEIRO qualquer: "))
lista = []

for i in range(2, num + 1):
    if i % 7 == 0:
        continue
    if str(i)[-1] == '5' or str(i)[-1] == '0':
        continue
    if i % 3 == 0:
        continue
    if i % 2 == 0:
        continue
    lista.append(i)

if num in lista or num == 2 or num == 3 or num == 5 or num == 7:
    print("É primo!")
else:
    print("Não é primo!")"""
