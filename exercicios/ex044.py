print("========================================================")
print("""  ____    _    _____ _____ _____ _____ ____  ___    _    
 / ___|  / \  |  ___| ____|_   _| ____|  _ \|_ _|  / \   
| |     / _ \ | |_  |  _|   | | |  _| | |_) || |  / _ \  
| |___ / ___ \|  _| | |___  | | | |___|  _ < | | / ___ \ 
 \____/_/   \_\_|   |_____| |_| |_____|_| \_\___/_/   \_\
""")
print("""\n                      (  )   (   )  )
                        ) (   )  (  (
                     ( )  (    ) )
                     _____________
                    <_____________> ___
                    |             |/ _  |
                    |               | | |
                    |               |_| |
                 ___|             |\___/
                /    \___________/    |
                \_____________________/
""")
print("========================================================")

nome = str(input("\nQual seu NOME? ")).strip().title()

print("\nBom dia, {}!".format(nome.upper().title()))
print("""\n==================== CARDÁPIO ==========================
Café ............................................... R$3
Café com Leite ..................................... R$5
Cappuccino ........................................ R$12
Café dos Deuses .................................. R$100
========================================================""")
print("""\n===================== CÓDIGOS ==========================
Café ................................................. 1
Café com Leite ....................................... 2
Cappuccino ........................................... 3
Café dos Deuses ...................................... 4
========================================================""")

opcao = int(input("\nQual BEBIDA você deseja? "))

valorCafe = 3
valorCafeComLeite = 5
valorCappuccino = 12
valorCafeDosDeuses = 100

print("""\n================= FORMAS DE PAGAMENTO ==================
DINHEIRO/CHEQUE ...................................... 1
CARTÃO ............................................... 2
========================================================""")

forma = int(input("\nQual a FORMA DE PAGAMENTO? "))

if forma == 1:
    print("\nComo você escolheu pagar no dinheiro/cheque, você ganhou 10% de desconto!")
    if opcao == 1:
        print("\nVALOR TOTAL: R${:.2f}".format(valorCafe - (valorCafe * 0.1)))
    elif opcao == 2:
        print("\nVALOR TOTAL: R${:.2f}".format(valorCafeComLeite - (valorCafeComLeite * 0.1)))
    elif opcao == 3:
        print("\nVALOR TOTAL: R${:.2f}".format(valorCappuccino - (valorCappuccino * 0.1)))
    elif opcao == 4:
        print("\nVALOR TOTAL: R${:.2f}".format(valorCafeDosDeuses - (valorCafeDosDeuses * 0.1)))

if forma == 2:
    print("""\n================= À VISTA OU PARCELADO =================
À VISTA .............................................. 1
PARCELADO ............................................ 2
========================================================""")
    formaCartao = int(input("\nVocê desejar pagar à vista ou parcelar? "))
    if formaCartao == 1:
        print("\nComo você escolheu pagar à vista no cartão, você ganhou 5% de desconto!")
        if opcao == 1:
            print("\nVALOR TOTAL: R${:.2f}".format(valorCafe - (valorCafe * 0.05)))
        elif opcao == 2:
            print("\nVALOR TOTAL: R${:.2f}".format(valorCafeComLeite - (valorCafeComLeite * 0.05)))
        elif opcao == 3:
            print("\nVALOR TOTAL: R${:.2f}".format(valorCappuccino - (valorCappuccino * 0.05)))
        elif opcao == 4:
            print("\nVALOR TOTAL: R${:.2f}".format(valorCafeDosDeuses - (valorCafeDosDeuses * 0.05)))
    if formaCartao == 2:
        parcelas = int(input("Em quantas vezes você deseja parcelar? "))
        if parcelas <= 2 and opcao == 1:
            print("\nVALOR TOTAL: R${:.2f}\nVALOR DA PARCELA: R${:.2f}".format(valorCafe, valorCafe / parcelas))
        elif parcelas <= 2 and opcao == 2:
            print("\nVALOR TOTAL: R${:.2f}\nVALOR DA PARCELA: R${:.2f}".format(valorCafeComLeite, valorCafeComLeite / parcelas))
        elif parcelas <= 2 and opcao == 3:
            print("\nVALOR TOTAL: R${:.2f}\nVALOR DA PARCELA: R${:.2f}".format(valorCappuccino, valorCappuccino / parcelas))
        elif parcelas <= 2 and opcao == 4:
            print("\nVALOR TOTAL: R${:.2f}\nVALOR DA PARCELA: R${:.2f}".format(valorCafeDosDeuses, valorCafeDosDeuses / parcelas))
        if parcelas > 3:
            print("\nComo você escolheu parcelar em 3x ou mais, sua compra teve um reajuste de 20% de juros!")
            if opcao == 1:
                print("\nVALOR TOTAL: R${:.2f}\nVALOR DA PARCELA: R${:.2f}".format(valorCafe + (valorCafe * 0.2), ((valorCafe + (valorCafe * 0.2)) / parcelas)))
            elif opcao == 2:
                print("\nVALOR TOTAL: R${:.2f}\nVALOR DA PARCELA: R${:.2f}".format(valorCafeComLeite + (valorCafeComLeite * 0.2), ((valorCafeComLeite + (valorCafeComLeite * 0.2)) / parcelas)))
            elif opcao == 3:
                print("\nVALOR TOTAL: R${:.2f}\nVALOR DA PARCELA: R${:.2f}".format(valorCappuccino + (valorCappuccino * 0.2), ((valorCappuccino + (valorCappuccino * 0.2)) / parcelas)))
            elif opcao == 4:
                print("\nVALOR TOTAL: R${:.2f}\nVALOR DA PARCELA: R${:.2f}".format(valorCafeDosDeuses + (valorCafeDosDeuses * 0.2), ((valorCafeDosDeuses + (valorCafeDosDeuses * 0.2)) / parcelas)))

print("\nMuito obrigado por comprar conosco! Volte sempre!")
