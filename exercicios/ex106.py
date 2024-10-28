from time import sleep
import io
import sys


def capturar_help(objeto):
    buffer = io.StringIO()
    sys.stdout = buffer
    help(objeto)
    sys.stdout = sys.__stdout__
    return buffer.getvalue()


def escreva(texto, style=0, text=0, background=0):
    tamanhoLinha = len(texto) + 4
    print(f"\033[{style};{text};{background}m~" * tamanhoLinha)
    print(f"{texto:^{tamanhoLinha}}")
    print(("~" * tamanhoLinha) + "                                                                                                                                                                                                                                                                                                           \033[m\n", end="")


while True:
    escreva("SISTEMA DE AJUDA PYHELP", 1, 0, 42)
    flag = str(input("Função ou Biblioteca > ").strip().lower())
    if flag == "fim":
        escreva("ATÉ LOGO!", 1, 0, 41)
        sleep(1)
        break
    escreva(f'Acessando o manual do comando "{flag}"', 1, 0, 46)
    sleep(1)
    help_texto = capturar_help(flag)
    escreva(help_texto, 0, 30, 107)
