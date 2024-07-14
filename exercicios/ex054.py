from datetime import date

print(""" __  __       _            _     _           _      
|  \/  | __ _(_) ___  _ __(_) __| | __ _  __| | ___ 
| |\/| |/ _` | |/ _ \| '__| |/ _` |/ _` |/ _` |/ _ |
| |  | | (_| | | (_) | |  | | (_| | (_| | (_| |  __/
|_|  |_|\__,_|_|\___/|_|  |_|\__,_|\__,_|\__,_|\___|\n""")

soma = 0

for i in range(1, 8):
    anoNascimento = int(input("Informe ANO DE NASCIMENTO da {}° pessoa: ".format(i)))
    if date.today().year - anoNascimento <= 17:
        soma += 1

if 7 - soma == 0:
    print("\nTodos ainda NÃO atingiram a MAIORIDADE!")
elif soma == 0:
    print("\nTodos JÁ atingiram a MAIORIDADE!")
else:
    print("\nNúmero de pessoas que ainda NÃO atingiram a MAIORIDADE: {}".format(soma))
    print("Número de pessoas que JÁ atingiram a MAIORIDADE: {}".format(7 - soma))
