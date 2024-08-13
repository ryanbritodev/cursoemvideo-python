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
        

lista = []

for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionando ao final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1

# num = int(input("Digite o 1° valor: "))
# valores.append(num)
# print("Adicionado ao final da lista...")

# for cont in range(2, 6):
#     num = int(input(f"Digite o {cont}° valor: "))
#     for indice in range(0, len(valores)):
#         if num > valores[len(valores) - 1] or num == valores[len(valores) - 1]:
#             valores.append(num)
#             print(f"Adicionado ao final da lista...")
#             break
#         elif num < valores[0] or num == valores[0]:
#             valores.insert(0, num)
#             print(f"Adicionado ao início da lista...")
#             break

print("=-" * 30)
print(f"Os valores digitados em ordem foram {lista}")
