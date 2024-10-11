from time import sleep


# Flush não liga o Buffer de tela, printando os número no mesmo tempo em que o sleep() foi setado
# Caso não tivesse, em algumas versões mais antigas do Pycharm, ele só printaria depois da soma do tempo estipulado
def contador(inicio, fim, passo):
    if fim > inicio:
        if passo == 0:
            passo = 1
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ", flush=True)
            sleep(0.25)
        print("FIM!", end="")
    elif inicio > fim:
        if passo < 0:
            for i in range(inicio, fim - 1, passo):
                print(i, end=" ", flush=True)
                sleep(0.25)
            print("FIM!", end="")
        elif passo > 0:
            passo = passo * -1
            for i in range(inicio, fim - 1, passo):
                print(i, end=" ", flush=True)
                sleep(0.25)
            print("FIM!", end="")
        else:
            passo = -1
            for i in range(inicio, fim - 1, passo):
                print(i, end=" ", flush=True)
                sleep(0.25)
            print("FIM!", end="")
    else:
        print("O início e o fim são iguais, logo, não tem pra onde andar!")


print("-=" * 20)
print("Contagem de 1 até 10 de 1 em 1")
contador(1, 10, 1)

# Quebra de Linha
print()

print("-=" * 20)
print("Contagem de 10 até 0 de 2 em 2")
contador(10, -1, -2)

print()
print("-=" * 20)

print("Agora é sua vez de personalizar a contagem!")
comeco = int(input("Início: "))
final = int(input("Fim:    "))
passada = int(input("Passo:  "))
print("-=" * 20)
if passada != 0:
    print(f"Contagem de {comeco} até {final} de {passada} em {passada}")
else:
    print(f"Contagem de {comeco} até {final} de 1 em 1")
contador(comeco, final, passada)
