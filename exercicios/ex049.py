print(""" _____  _    ____  _   _   _    ____    _    
|_   _|/ \  | __ )| | | | / \  |  _ \  / \   
  | | / _ \ |  _ \| | | |/ _ \ | | | |/ _ \  
  | |/ ___ \| |_) | |_| / ___ \| |_| / ___ \ 
  |_/_/   \_\____/ \___/_/   \_\____/_/   \_|\n""")

numero = int(input("Digite um NÚMERO para ver sua TABUADA: "))

print("\nTABUADA DO {}".format(numero))

multiplicador = 1

for i in range(0, 10):
    print("{} x {:2} = {}".format(numero, multiplicador, numero * multiplicador))
    multiplicador += 1
