print(""" _____ ____  ___  //\  _   _  ____ _   _ _     ___  ____  
|_   _|  _ \|_ _||/_\|| \ | |/ ___| | | | |   / _ \/ ___| 
  | | | |_) || |  /_\ |  \| | |  _| | | | |  | | | \___ \ 
  | | |  _ < | | / _ \| |\  | |_| | |_| | |__| |_| |___) |
  |_| |_| \_\___/_/ \_\_| \_|\____|\___/|_____\___/|____/ 
""")

lado1 = float(input("TAMANHO DO 1° SEGMENTO DO 🛆: "))
lado2 = float(input("TAMANHO DO 2° SEGMENTO DO 🛆: "))
lado3 = float(input("TAMANHO DO 3° SEGMENTO DO 🛆: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    print("\nO 🛆 PODE existir!")
    if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print("Ele é um 🛆 ISÓSCELES")
    elif lado1 == lado2 == lado3:
        print("Ele é um 🛆 EQUILÁTERO")
    elif lado1 != lado2 != lado3:
        print("Ele é um 🛆 ESCALENO")
else:
    print("O 🛆 NÃO pode existir!")
