import sys

print("""  ____      _            _           _                 
 / ___|__ _| | ___ _   _| | __ _  __| | ___  _ __ __ _ 
| |   / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |
| |__| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |
 \____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|
 / __/ _ \| '_ ` _ \                                   
| (_| (_) | | | | | |                                  
_\___\___/|_| |_| |_|                                  
\ \      / / |__ (_) | ___                             
 \ \ /\ / /| '_ \| | |/ _ \                            
  \ V  V / | | | | | |  __/                            
   \_/\_/  |_| |_|_|_|\___|                            \n""")

num1 = int(input("DIGITE O 1° VALOR: "))
num2 = int(input("DIGITE O 2° VALOR: "))

menu = """\n==============================
          🧮 MENU 🧮
==============================
1. ➕  Adição
2. ✖️  Multiplicação
3. 🔍  Maior Valor
4. 🔄  Inserir Novos Números
5. ❌  Sair
==============================
"""

print(menu)

opcao = int(input("INFORME A OPÇÃO DESEJADA: "))
maior = 0
loop = True

while loop:
    if opcao < 1 or opcao > 5:
        opcao = int(input("\nOPÇÃO INVÁLIDA!\nINFORME A OPÇÃO DESEJADA NOVAMENTE: "))
    if opcao == 1:
        print("\nRESULTADO DA SOMA = {}".format(num2 + num1))
        print(menu)
        opcao = int(input("INFORME A OPÇÃO DESEJADA: "))
    elif opcao == 2:
        print("\nRESULTADO DA MULTIPLICAÇÃO = {}".format(num2 * num1))
        print(menu)
        opcao = int(input("INFORME A OPÇÃO DESEJADA: "))
    elif opcao == 3:
        if num1 == num2:
            print("\nOS VALORES SÃO IGUAIS!")
            print(menu)
            opcao = int(input("INFORME A OPÇÃO DESEJADA: "))
        elif num2 > num1:
            print("\nO MAIOR VALOR É {}!".format(num2))
            print(menu)
            opcao = int(input("INFORME A OPÇÃO DESEJADA: "))
        else:
            print("\nO MAIOR VALOR É {}!".format(num1))
            print(menu)
            opcao = int(input("INFORME A OPÇÃO DESEJADA: "))
    elif opcao == 4:
        num1 = int(input("\nDIGITE O 1° VALOR: "))
        num2 = int(input("DIGITE O 2° VALOR: "))
        print(menu)
        opcao = int(input("INFORME A OPÇÃO DESEJADA: "))
    elif opcao == 5:
        print("\nENCERRANDO O PROGRAMA...")
        loop = False
