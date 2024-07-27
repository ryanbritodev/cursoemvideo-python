print(""" ____       _                           
|  _ \ __ _| | __ ___   ___ __ __ _ ___ 
| |_) / _` | |/ _` \ \ / / '__/ _` / __|
|  __/ (_| | | (_| |\ V /| | | (_| \__ |
|_|   \__,_|_|\__,_| \_/ |_|  \__,_|___/\n""")


palavras = ("aprender", "programar", "linguagem", "python",
            "curso", "gratis", "estudar", "praticar", "trabalhar",
            "mercado", "programador", "futuro")

for palavra in range(0, len(palavras)):
    resultado = f"Na palavra {str(palavras[palavra]).upper()} temos "
    if "a" in palavras[palavra]:
        quantidade = str(palavras[palavra]).count("a")
        resultado += "a " * quantidade
    if "e" in palavras[palavra]:
        quantidade = str(palavras[palavra]).count("e")
        resultado += "e " * quantidade
    if "i" in palavras[palavra]:
        quantidade = str(palavras[palavra]).count("i")
        resultado += "i " * quantidade
    if "o" in palavras[palavra]:
        quantidade = str(palavras[palavra]).count("o")
        resultado += "o " * quantidade
    if "u" in palavras[palavra]:
        quantidade = str(palavras[palavra]).count("u")
        resultado += "u " * quantidade
    print(resultado.strip())
