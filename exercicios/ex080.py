print(""" ___                         /\/|       
|_ _|_ __  ___  ___ _ __ ___|/\/_  ___  
 | || '_ \/ __|/ _ \ '__/ __/ _` |/ _ \ 
 | || | | \__ \  __/ | | (_| (_| | (_) |
|___|_| |_|___/\___|_|  \___\__,_|\___/ 
                         )_)            \n""")

valores = []

for cont in range(1, 6):
    valor = int(input(f"Digite o {cont}° valor: "))
    valores.append(valor)
    if valor > valores[4]:
        print("Adicionando ao final da lista...")
        