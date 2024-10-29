import time


def leiaInt(pergunta):
    while True:
        try:
            numero = int(input(f"{pergunta}"))
            while numero > 3 or numero <= 0:
                print(f"{"\033[1:31m"}ERRO! Digite um número dentre as opções do menu.{f"\033[m"}")
                numero = int(input(f"{pergunta}"))
            return numero
        except ValueError:
            print(f"{"\033[1:31m"}ERRO! Digite um número inteiro válido.{f"\033[m"}")
        except KeyboardInterrupt:
            print(f"{"\033[1:31m"}O usuário preferiu não digitar esse número.{f"\033[m"}")
            exit()


def leiaFloat(pergunta):
    while True:
        try:
            numero = float(input(f"{pergunta}"))
            return numero
        except ValueError:
            print(f"{"\033[1:31m"}ERRO! Digite um número real válido.{f"\033[m"}")
        except KeyboardInterrupt:
            print(f"{"\033[1:31m"}O usuário preferiu não digitar esse número.{f"\033[m"}")
            exit()


def criarArquivo():
    arquivo = open("ex115.txt", "w", encoding="UTF-8")
    arquivo.write("""----------------------------------
        PESSOAS CADASTRADAS
----------------------------------""")
    arquivo.close()


def leiaIdade(pergunta):
    while True:
        try:
            numero = int(input(f"{pergunta}"))
            return numero
        except ValueError:
            print(f"{"\033[1:31m"}ERRO! Digite um número inteiro válido.{f"\033[m"}")
        except KeyboardInterrupt:
            print(f"{"\033[1:31m"}O usuário preferiu não digitar esse número.{f"\033[m"}")
            exit()


def lerArquivo():
    arquivo = open("ex115.txt", "r", encoding="UTF-8")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()


def cadastroArquivo():
    cadastro = """----------------------------------
          NOVO CADASTRO
----------------------------------"""
    arquivo = open("ex115.txt", "a", encoding="UTF-8")
    print(cadastro)
    nome = str(input("Nome: ")).strip().title()
    idade = leiaIdade("Idade: ")
    idadeFormatada = f"{idade} anos"
    arquivo.write("\n{:<17}{:>17}".format(nome, idadeFormatada))


def sairPrograma():
    print("""----------------------------------
     SAINDO DO SISTEMA... ATÉ!
----------------------------------""")
    time.sleep(1)
    exit()
