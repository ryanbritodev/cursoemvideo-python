# Laços de Repetição/Iteração com Variável de Controle FOR
""" Se quisermos que um personagem chegue a maçã, não precisamos ficar digitando por incontáveis vezes o comado de
"andar", nós podemos simplesmente criar uma repetição que acaba até que ele encontre a maçã, economizando espaço na
memória e evitando a repetição excessiva. """

indice = 0
blocos = ["BLOCO", "BLOCO", "VAZIO", "MOEDA", "BLOCO", "VAZIO","BLOCO", "BLOCO", "VAZIO", "MOEDA", "MAÇÃ"]

for i in range(1, 10):
    print("PASSO")
print("PEGA\n")

for i in range(0, 3):
    print("PASSO")
    print("PULA")
print("PASSO")
print("PEGA\n")

for i in range(0, 3):
    if "MOEDA":
        print("PEGA")
    print("PASSO")
    print("PULA")
print("PASSO")
print("PEGA")
