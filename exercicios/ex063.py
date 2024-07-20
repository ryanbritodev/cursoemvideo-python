import sys

print(""" ____                    //\            _       
/ ___|  ___  __ _ _   _ |/_\|_ __   ___(_) __ _ 
\___ \ / _ \/ _` | | | |/ _ \ '_ \ / __| |/ _` |
 ___) |  __/ (_| | |_| |  __/ | | | (__| | (_| |
|____/ \___|\__, |\__,_|\___|_| |_|\___|_|\__,_|
|  ___(_) |__  |_|_  _ __   __ _  ___ ___(_)    
| |_  | | '_ \ / _ \| '_ \ / _` |/ __/ __| |    
|  _| | | |_) | (_) | | | | (_| | (_| (__| |    
|_|   |_|_.__/ \___/|_| |_|\__,_|\___\___|_|    """)

n = int(input("\nDigite um número para saber os primeiros\nelementos da Sequência de Fibonacci: "))
anteantecessor = 0
antecessor = 1
contador = 2

while True:
    if n < 1:
        print("\nNÚMERO INVÁLIDO!")
        n = int(input("\nDigite um número para saber os primeiros\nelementos da Sequência de Fibonacci: "))
    else:
        break

if n == 1:
    print("0 → ", end="")
elif n >= 2:
    print("0 → 1 → ", end="")

while contador < n:
    fibonacci = anteantecessor + antecessor
    print(fibonacci, "→ ", end="")
    anteantecessor = antecessor
    antecessor = fibonacci
    contador += 1

print("FIM!")
