from random import randint
from time import sleep

print("""     _                         _                          
    | | ___   __ _  ___     __| | ___                     
 _  | |/ _ \ / _` |/ _ \   / _` |/ _ \                    
| |_| | (_) | (_| | (_) | | (_| |  __/                    
 \___/ \___/ \__, |\___/   \__,_|\___|                    
    _       _|___/    _       _                /\/|       
   / \   __| (_)_   _(_)_ __ | |__   __ _  ___|/\/_  ___  
  / _ \ / _` | \ \ / / | '_ \| '_ \ / _` |/ __/ _` |/ _ \ 
 / ___ \ (_| | |\ V /| | | | | | | | (_| | (_| (_| | (_) |
/_/   \_\__,_|_| \_/ |_|_| |_|_| |_|\__,_|\___\__,_|\___/ 
                                           )_)            \n""")

computador = int(randint(1, 10))

print("O computador está pensando...\n")
sleep(3)
print("O computador escolheu um número entre 1 e 10\nTente adivinhar qual foi o número pensado!\n")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1
    if jogador < 1 or jogador > 10:
        print("Valor inválido! Digite um número entre 1 e 10")
    if jogador == computador:
        acertou = True
    if jogador != computador and jogador < computador and 1 <= jogador <= 10:
        print("Um pouco mais... Tente mais uma vez")
    elif jogador != computador and jogador > computador and 1<= jogador <= 10:
        print("Um pouco menos... Tente mais uma vez")
print("Parabéns! Você acertou com {} tentativas".format(palpites))

"""
palpite = int(input("Digite o seu palpite: "))

while palpite != numPensado:
    if palpite < 1 or palpite > 10:
        palpite = int(input("Palpite inválido!\nDigite um número entre 1 e 10: "))
    else:
        palpite = int(input("Palpite errado!\nDigite o seu palpite novamente: "))
print("\nParabéns, você acertou! O número pensado foi {}!".format(numPensado))
"""
