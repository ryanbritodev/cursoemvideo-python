def leiaInt(pergunta):
    while True:
        try:
            numero = int(input(f"{pergunta}"))
            return numero
        except ValueError:
            print(f"{"\033[1:31m"}ERRO! Digite um número inteiro válido.{f"\033[m"}")
        except KeyboardInterrupt:
            print(f"{"\033[1:31m"}O usuário preferiu não digitar esse número.{f"\033[m"}")
            return 0


def leiaFloat(pergunta):
    while True:
        try:
            numero = float(input(f"{pergunta}"))
            return numero
        except ValueError:
            print(f"{"\033[1:31m"}ERRO! Digite um número real válido.{f"\033[m"}")
        except KeyboardInterrupt:
            print(f"{"\033[1:31m"}O usuário preferiu não digitar esse número.{f"\033[m"}")
            return 0


num = leiaInt("Digite um Número Inteiro: ")
num2 = leiaFloat("Digite um Número Real: ")

print(f"O Valor Inteiro digitado foi {num} e o Valor Real foi {num2}")
