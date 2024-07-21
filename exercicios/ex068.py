from random import randint

print("=" * len("-----------------------------------"))

print(""" ____                              
|  _ \ __ _ _ __    ___  _   _     
| |_) / _` | '__|  / _ \| | | |    
|  __/ (_| | |    | (_) | |_| |    
|_|_  \__,_|_|     \___/ \__,_|___ 
 /_/ _ __ ___  _ __   __ _ _ _|__ |
|_ _| '_ ` _ \| '_ \ / _` | '__|/ /
 | || | | | | | |_) | (_| | |  |_| 
|___|_| |_| |_| .__/ \__,_|_|  (_) 
              |_|                  """)

print("=" * len("-----------------------------------"))

print("\nVAMOS JOGAR?\n")

soma = resultado = cont = 0

while True:
    jogadaHumano = int(input("Diga um valor: "))
    parOuImpar = str(input("Par ou Ímpar? [P/I] ").replace(" ", "").upper())
    jogadaComputador = randint(1, 10)
    soma = jogadaComputador + jogadaHumano
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"
    print(f"\nVocê jogou {jogadaHumano} e o computador {jogadaComputador}. O total da soma vale {soma}, deu {resultado}!")
    if resultado[0] == parOuImpar:
        print("\nVocê VENCEU!")
        print("Vamos jogar novamente...\n")
        cont += 1
    else:
        print("\nVocê PERDEU!")
        print(f"GAME OVER! Você venceu {cont} vezes.")
        break
