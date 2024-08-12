listaNum = []
listaPar = []
listaImpar = []

for c in range(1, 8):
    num = int(input(f"Digite o {c}° número: "))
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
