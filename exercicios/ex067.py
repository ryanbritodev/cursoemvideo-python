cores = {
    "vermelho": "\033[1;31m",
    "limpa": "\033[m"
}

print(""" ____                                    
/ ___| _   _ _ __   ___ _ __             
\___ \| | | | '_ \ / _ \ '__|            
 ___) | |_| | |_) |  __/ |               
|____/ \__,_| .__/ \___|_|       _       
|_   _|_ _| |_|  _   _  __ _  __| | __ _ 
  | |/ _` | '_ \| | | |/ _` |/ _` |/ _` |
  | | (_| | |_) | |_| | (_| | (_| | (_| |
  |_|\__,_|_.__/ \__,_|\__,_|\__,_|\__,_|""")

contador = 1

while True:
    tabuada = int(input("\nQuer ver a tabudada de qual valor? "))
    tamanhoMaiorTermo = len("TABUADA DO NÚMERO {}".format(tabuada))
    if tabuada < 1:
        print(f"\nVALOR NEGATIVO INFORMADO!\n{cores['vermelho']}PROGRAMA ENCERRADO{cores['limpa']}")
        break
    else:
        print("\n" + "=" * tamanhoMaiorTermo)
        print(f"TABUADA DO {tabuada}")
        print("=" * tamanhoMaiorTermo)
        for contador in range(1, 11):
            print(f"{tabuada} x {contador:2} = {tabuada * contador}")
            contador += 1
