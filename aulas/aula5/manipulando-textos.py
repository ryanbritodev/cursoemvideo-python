frase = "Curso em Vídeo Python"
# C u r s o   e m   V í  d  e  o     P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# Frase normal
print(frase)

# Fatiamento
print(frase[9])  # Exibe na tela somente o índice 9 da string, no caso, a letra V maiúscula
print(frase[9:13])  # Exibe na tela somente do índice 9 ao 12, onde ele SEMPRE vai começar certinho no número e no final excluir o índice, deixando somente o anterior (no caso da string, o 12)
print(frase[9:21])  # Exibe na tela somente do índice 9 até o 20, excluindo o 21 (não é recomendado colocar um índice inexistente)
print(frase[9:21:2])  # Exibe na tela a mesma string fatiada anteriormente porém pulando de 2 e 2 índices
print(frase[::2]) # Exibe na tela a string inteira, pulando de dois e dois índices
print(frase[:5])  # Exibe tudo antes do índice 5 (quando omitimos o ínicio do fatiamente, ele começa pelo índice 0)
print(frase[15:])  # Exibe tudo depois do índice 15 até o final da string
print(frase[9::3])  # Começa no índice 9, indo até o final, pulando 3 índices ao mesmo tempo

# Análise
print(len(frase))  # Vem da palavra "length", que significa comprimento (a frase tem 21 caracteres, indo do índice 0 ao 20)
print(frase.count("o")) # Conta a quantidade de vezes que a letra "o" minúsculo aparece na string
print(frase.count("o", 0, 13))  # Conta a quantidade de letras "o" minúsculas na fatia da string que vai do índice 0 ao 13 (excluindo o último índice e só contabilizando o anterior, no caso o 12)
print(frase.find("deo"))  # Quantas vezes ele encontrou o padrão "deo" na string, indicando aonde ele começou
print(frase.find("Android"))  # Se colocarmos no find uma string que não existe, ele retorna o valor -1 (não foi encontrado)
print("Curso" in frase)  # O operador "in" verifica se existe dentro da string o conjunto de caracteres "Curso", retornando o dado primitivo booleano "True"

# Transformação
# String são IMUTÁVEIS, só podem ser mudadas através dos métodos de transformação
print(frase.replace("Python", "Android"))  # Substitui na string a palavra "Python" por "Android"
print(frase.upper())  # Método que transforma tudo que for minúsculo em maiúsculo, mantendo aquilo que já estava maiúsculo
print(frase.upper().count("O")) # Conta a quantidade de letras "O" maiúsculas dentro da string após ser transformada em maiùscula
print(frase.lower())  # Método que transforma tudo que for maiúsculo em minúsculo, mantendi aquilo que já for minúsculo
print(frase.capitalize())  # Joga todos os caracteres para minúsculo e deixa somente o primeiro em minúsculo
print(frase.title())  # Quebra todos os caracteres em palavras e deixa somente a primeira letra em maiúsculo
fraseEspaco = "   Aprenda Python   "
print(fraseEspaco.strip())  # Remove todos os espaços inúteis no ínicio e no final da string
print(len(fraseEspaco)) # Tamanho da string com os espaços
print(len(fraseEspaco.strip())) # Tamanho da string sem os espaços
print(fraseEspaco.rstrip())  # Remove os espaços a direita da string
print(fraseEspaco.lstrip()) # Remove os espaços a esquerda da string

# Divisão
print(frase.split())  # Divide uma string em uma lista, separando cada elemento pelos espaços entre eles
# C u r s o   e m   V í d e o   P y t h o n
# 0 1 2 3 4   0 1   0 1 2 3 4   0 1 2 3 4 5
#     0        1        2            3
fraseDividida = frase.split()
print(fraseDividida[0], fraseDividida[1], fraseDividida[2], fraseDividida[3])

# Junção
print("-".join(frase))
print("-".join(frase.split()))
