valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

# Com a função ENUMERATE, podemos descobrir o índice e o valor em
# que o elemento está
for c, v in enumerate(valores):
    print(f"No {c+1}ª posição encontrei o valor {v}")
print("Cheguei ao final da lista")
