jogadores = []

while True:
    print("-" * 35)
    nome = str(input("Nome do jogador: ")).strip().title()
    partidas = int(input(f"Quantas partidas {nome} jogou? "))
    gols = []
    for i in range(partidas):
        gols.append(int(input(f"Quantos gols na partida {i + 1}? ")))
    while True:
        flag = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if flag != "S" and flag != "N":
            print("Opção inválida! Tente novamente")
        else:
            break
    jogadores.append({"nome": nome, "gols": gols, "total": sum(gols)})
    if flag == "N":
        break

print("-=" * 35)

print("Cód. Nome               Gols      Total")
print("---------------------------------------")

codigo = 0

for jogador in jogadores:
    print(f'{codigo:>4} {jogador["nome"]:<15} {jogador["gols"]} {jogador["total"]:<5}')
    codigo += 1
print("---------------------------------------")

while True:
    dadoJogador = int(input("Mostrar dados de qual jogador (ou 999 para sair)? "))
    if dadoJogador > len(jogadores) - 1 and dadoJogador != 999:
        print(f"ERRO! Não existe jogador com o código {dadoJogador}! Tente novamente")
    elif dadoJogador < 0:
        print(f"ERRO! Não existe jogador com o código {dadoJogador}! Tente novamente")
    elif dadoJogador != 999:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[dadoJogador]["nome"]}:")
        for i, gols in enumerate(jogadores[dadoJogador]["gols"]):
            print(f"   No jogo {i + 1} fez {gols} gols.")
        print("---------------------------------------")
    else:
        print("<< VOLTE SEMPRE >>")
        break
