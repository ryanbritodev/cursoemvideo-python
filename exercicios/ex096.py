# Faça um programa que tenha uma função chamada área(), que receba as dimansõas de um terreno retangular (largura a comprimento) a mostre a área do terreno.

print(" Controle de Terrenos ")
print("-" * 22)

largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))


def area(lar, com):
    areaTotal = lar * com
    print(f"A área de um terreno {lar}x{com} é de {areaTotal}m².")


area(largura, comprimento)
