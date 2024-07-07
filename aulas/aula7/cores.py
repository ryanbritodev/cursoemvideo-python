# COLORINDO O TERMINAL

"""
Podemos colorir com muitos módulos, como o "Colorize" Padrão
ANSI de normalização internacional que possui os "escapes sequences",
servindo para várias linguagens. Ele é iniciado com um contra
barra "\" e em seguida, vem um código, como por exemplo o de
cores, que começa com "\033[m", onde entre o colchete e a letra "m"
adicionamos o código do comportamento (style), texto (text) e a cor
de fundo (background). Todos eles devem ser separados com um ponto e
vírgula ";".
"""

# \033[   0;     33;    44m
#       style   text   back

""" 
STYLE 
0 - Nada
1 - Negrito
4 - Sublinhado
7 - Negativo
"""

"""
   text                  background
30      black        preto          40
31      red          vermelho       41
32      green        verde          42
33      yellow       amarelo        43
34      blue         azul           44
35      Magenta      Magenta        45
36      cyan         ciano          46
37      grey         cinza          47
97      white        branco        107
"""

# Fundo vermelho com texto branco
print("\033[0;107;41mOlá Mundo")

# Fundo roxo com texto amarelo sublinhado
print("\033[4;33;44mOlá Mundo")

# Texto roxo com fundo amarelo
print("\033[0;35;43mOlá Mundo")

# Fundo verde com texto branco
print("\033[97;42mOlá Mundo")

# Padrão do terminal
print("\033[mOlá Mundo")

# Fundo branco com texto preto (invertido)
print("\033[30;107mOlá Mundo")

print("\033[m")

print("\033[1;31;43mOlá, Mundo\033[m")
print("\033[4;30;45mOlá, Mundo\033[m")
print("\033[0;30;107mOlá, Mundo\033[m")
print("\033[7;30;107mOlá, Mundo\033[m")

a = 3
b = 5

print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m".format(a, b))

nome = "Ryan"
print("Olá! Muito prazer em te conhecer, {}{}{}!".format("\033[1;97m", nome, "\033[m"))

cores = {"limpa": "\033[m",
         "vermelho": "\033[31m",
         "amarelo": "\033[33m",
         "pretoebranco": "\033[30;107m"}

print("Olá! Muito prazer em te conhecer, {}{}{}!".format(cores["pretoebranco"], nome, cores["limpa"]))
