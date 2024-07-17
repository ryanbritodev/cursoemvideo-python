print(""" ____                    //\            _       
/ ___|  ___  __ _ _   _ |/_\|_ __   ___(_) __ _ 
\___ \ / _ \/ _` | | | |/ _ \ '_ \ / __| |/ _` |
 ___) |  __/ (_| | |_| |  __/ | | | (__| | (_| |
|____/ \___|\__, |\__,_|\___|_| |_|\___|_|\__,_|
|  ___(_) |__  |_|_  _ __   __ _  ___ ___(_)    
| |_  | | '_ \ / _ \| '_ \ / _` |/ __/ __| |    
|  _| | | |_) | (_) | | | | (_| | (_| (__| |    
|_|   |_|_.__/ \___/|_| |_|\__,_|\___\___|_|    """)

n = int(input("\nDigite um número para saber os primeiros elementos da Sequência de Fibonacci: "))
antecessor = 2
sucessor = 3

fibonacci = 1

while fibonacci < n:
    antecessor += sucessor
    fibonacci += 1
    print(antecessor)
