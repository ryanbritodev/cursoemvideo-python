from random import randint
from time import sleep

print("""{}     _       _                     //\  
    | | ___ | | _____ _ __  _ __  |/_\| 
 _  | |/ _ \| |/ / _ \ '_ \| '_ \ / _ \ 
| |_| | (_) |   <  __/ | | | |_) | (_) |
 \___/ \___/|_|\_\___|_| |_| .__/ \___/ 
                           |_|          
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___){}""".format("\033[1m", "\033[m"))

escolhaComputador = randint(1, 3)

if escolhaComputador == 1:
    escolhaComputador = "pedra"
elif escolhaComputador == 2:
    escolhaComputador = "papel"
elif escolhaComputador == 3:
    escolhaComputador = "tesoura"

print("""\n{}Bem-vindo ao jogo de Jokenpô em Python!{}\n
{}REGRAS DO JOGO:{}
{}1. Você pode escolher entre PEDRA, PAPEL ou TESOURA.
2. O computador fará uma escolha aleatória entre PEDRA, PAPEL e TESOURA.
3. As regras para determinar o vencedor são:
- PEDRA ganha de TESOURA
- PAPEL ganha de PEDRA
- TESOURA ganha de PAPEL
4. Se ambos escolherem o mesmo, o jogo empata.{}""".format("\033[1m", "\033[m", "\033[1;33m", "\033[m", "\033[1m", "\033[m"))

escolhaJogador = str(input("\nEscolha entre {}PEDRA{}, {}PAPEL{} e {}TESOURA{}: ".format("\033[1m", "\033[m", "\033[1m", "\033[m", "\033[1m", "\033[m"))).strip().lower()

print("\n{}VAMOS JOGAR?{}".format("\033[1;33m", "\033[m"))
sleep(2)
print("\n{}PEDRA{}".format("\033[1m", "\033[m"))
sleep(0.7)
print("{}PAPEL{}".format("\033[1m", "\033[m"))
sleep(0.7)
print("{}TESOURA!{}\n".format("\033[1m", "\033[m"))
sleep(0.5)

if escolhaJogador == escolhaComputador:
    print("{}EMPATE! Os dois jogadores escolheram {}{}!".format("\033[1;33m", escolhaComputador.upper(), "\033[m"))

# Derrota
if escolhaComputador == "pedra" and escolhaJogador == "tesoura":
    print("{}Você PERDEU! O computador escolheu PEDRA!{}".format("\033[1;31m", "\033[m"))
elif escolhaComputador == "papel" and escolhaJogador == "pedra":
    print("{}Você PERDEU! O computador escolheu PAPEL!{}".format("\033[1;31m", "\033[m"))
elif escolhaComputador == "tesoura" and escolhaJogador == "papel":
    print("{}Você PERDEU! O computador escolheu TESOURA!{}".format("\033[1;31m", "\033[m"))

# Vitória
if escolhaJogador == "pedra" and escolhaComputador == "tesoura":
    print("{}Você GANHOU! O computador escolheu TESOURA!{}".format("\033[1;32m", "\033[m"))
elif escolhaJogador == "papel" and escolhaComputador == "pedra":
    print("{}Você GANHOU! O computador escolheu PEDRA!{}".format("\033[1;32m", "\033[m"))
elif escolhaJogador == "tesoura" and escolhaComputador == "papel":
    print("{}Você GANHOU! O computador escolheu PAPEL!{}".format("\033[1;32m", "\033[m"))
