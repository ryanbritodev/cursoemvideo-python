nome = str(input("Nome do jogador: ")).strip().title()
partidas = int(input(f"Quantas partidas {nome} jogou? "))
gols = []
for i in range(partidas):
    gols.append(int(input(f"    Quantos gols na partida {i + 1}? ")))
print("-=" * 35)
jogador = {
    "nome": nome,
    "gols": gols,
    "total": sum(gols)
}
print(jogador)
print("-=" * 35)
for campos in jogador:
    valor = jogador[campos]
    print(f"O campo {campos} tem o valor {valor}.")
print("-=" * 35)
print(f"O jogador {jogador["nome"]} jogou {partidas} partidas.")
for c in range(partidas):
    print(f"    => Na partida {c + 1}, fez {gols[c]} gols.")
print(f"Foi um total de {sum(gols)} gols.")
