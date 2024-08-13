matriz = [int(input("Digite um valor para [0, 0]: ")),
          int(input("Digite um valor para [0, 1]: ")),
          int(input("Digite um valor para [0, 2]: ")),
          int(input("Digite um valor para [1, 0]: ")),
          int(input("Digite um valor para [1, 1]: ")),
          int(input("Digite um valor para [1, 2]: ")),
          int(input("Digite um valor para [2, 0]: ")),
          int(input("Digite um valor para [2, 1]: ")),
          int(input("Digite um valor para [2, 2]: "))]

print("=-" * 30)
print("""[  {}  ][  {}  ][  {}  ]
[  {}  ][  {}  ][  {}  ]
[  {}  ][  {}  ][  {}  ]""".format(matriz[0], matriz[1], matriz[2], matriz[3],
           matriz[4], matriz[5], matriz[6], matriz[7], matriz[8]))
print("=-" * 30)

somaPar = 0
segundaLinha = [matriz[3], matriz[4], matriz[5]]

for valor in matriz:
    if valor % 2 == 0:
        somaPar += valor

print(f"A soma dos valores pares é {somaPar}")
print(f"A soma dos valores da terceira coluna é {matriz[2] + matriz[5] + matriz[8]}")
print(f"O maior valor da segunda linha é {max(segundaLinha)}")
