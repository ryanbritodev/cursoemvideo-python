print(""" ____       _ __          _                           
|  _ \ __ _| /_/_ __   __| |_ __ ___  _ __ ___   ___  
| |_) / _` | | | '_ \ / _` | '__/ _ \| '_ ` _ \ / _ \ 
|  __/ (_| | | | | | | (_| | | | (_) | | | | | | (_) |
|_|   \__,_|_|_|_| |_|\__,_|_|  \___/|_| |_| |_|\___/ """)

frase = str(input("\nDigite uma FRASE qualquer: ")).lower()

fraseSemEspaco = "".join(frase.strip())
fraseAoContrario = fraseSemEspaco[::-1]

if fraseAoContrario == fraseSemEspaco:
    print("{}Sua frase É UM PALÍNDROMO!{}".format("\033[1;32m", "\033[m"))
else:
    print("{}Sua frase NÃO É UM PALÍNDROMO!{}".format("\033[1;31m", "\033[m"))
