def leiaInt(pergunta):
    while True:
        try:
            numero = int(input(f"{pergunta}"))
            return numero
        except ValueError:
            print(f"{"\033[1:31m"}ERRO! Digite um número inteiro válido.{f"\033[m"}")


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
