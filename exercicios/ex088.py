from random import randint
from time import sleep

print("=" * 30)
print("{:^30}".format("JOGO NA MEGA SENA"))
print("=" * 30)
jogos = int(input("Quantos jogos você quer que eu sorteie? "))
numeros = []

print(f"-=-=-= SORTEANDO {jogos} JOGOS -=-=-=")
for i in range(1, jogos + 1):
    print(f"Jogo {i}: ", end="")
    numeros = [randint(1,60), randint(1, 60),
               randint(1, 60), randint(1, 60),
               randint(1, 60), randint(1, 60)]
    while len(numeros) != len(set(numeros)):
        numeros = [randint(1, 60), randint(1, 60),
                   randint(1, 60), randint(1, 60),
                   randint(1, 60), randint(1, 60)]
    print(numeros)
    sleep(1)
print("-=-=-=-=   BOA SORTE!  -=-=-=-=")
