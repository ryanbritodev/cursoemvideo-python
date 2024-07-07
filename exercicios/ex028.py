from random import randint
from time import sleep

numPensado = int(randint(1, 5))

print("=-" * 6, "JOGO DE ADIVINHAÇÃO", "-=" * 6)
print("O computador está pensando...")
sleep(3)
print("O computador escolheu um número entre 1 e 5\nTente adivinhar qual foi o número pensado!")

palpite = int(input("Digite seu palpite: "))

print("PARABÉNS! VOCÊ ACERTOU =D" if palpite == numPensado else "QUE PENA! VOCÊ ERROU =/\nNÚMERO PENSADO: {}".format(numPensado))
