listaNum = [[], []]

for c in range(1, 8):
    num = int(input(f"Digite o {c}° número: "))
    if num % 2 == 0:
        listaNum[0].append(num)
    else:
        listaNum[1].append(num)

listaNum[0].sort()
listaNum[1].sort()

print("=-" * 30)
print(f"Os valores pares digitados foram: {listaNum[0]}")
print(f"Os valores ímpares digitados foram: {listaNum[1]}")
