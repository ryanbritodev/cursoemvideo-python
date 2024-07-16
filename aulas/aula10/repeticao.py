for c in range(1, 11):
    print(c, end=" ")
print("FIM")

# Mesmo laço utilizando o WHILE

c = 1
while c < 11:
    print(c, end=" ")
    c += 1
print("FIM\n")

# O laço WHILE serve tanto para quando não sabemos o limite, e para quando nós sabemos

for c in range(1, 4):
    n = int(input("Digite um valor: "))
print("FIM\n")

n = 1

# N funciona como uma "flag" de saída para o laço de repetição, algo que não seria possível com o laço de repetição "for"
while n != 0:
    n = int(input("Digite um valor: "))
print("FIM\n")

r = "S"

while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("FIM\n")

par = impar = 0

while n != 0:
    n = int(input("Digite um valor ou 0 para sair: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {par} números pares e {impar} números ímpares!")
print("FIM")
