# Funções em Python
# De uma forma geral, todas as funções em Python estão ligadas
# a uma única palavra: ROTINA

# O que é uma rotina? Algo que usamos constantemente
# Exemplos:
# print(), len(), input(), int(), float()
# Funções que já existem em Python

# Podemos fazer uma função que atenda uma necissidade de algo recorrente, como é por exemplo
# Muito usado aqui nas aulas dos cursos do Guanabara a impressão de linhas

# Podemos criar a função mostraLinha()

# def vem de DEFINIÇÃO de uma função personalizada

# Ao invés de imprimirmos uma linha com vários caracteres, podemos resumir para apenas um simples print()

def mostraLinha():
    print("-" * 30)


# Pycharm reclama se não colocarmos duas linhas separando
# a função do programa principal, que é esse que está logo abaixo

# Chamando as linhas com a função criada
mostraLinha()
print("{:^30}".format("SISTEMA DE ALUNOS"))
mostraLinha()
print()
mostraLinha()
print("{:^30}".format("CADASTRO DE FUNCIONÁRIOS"))
mostraLinha()
print()
mostraLinha()
print("{:^30}".format("ERRO DO SISTEMA"))
mostraLinha()


# Podemos ver que a estrutura desse código se repete muitas vezes
# Para podermos economizar espaço, uso da memória e processamento,
# Vamos criar a estruta da nova função, colocando apenas o essencial

def mensagem(msg):
    # Nessa função, passamos como parâmetro somente a funçõa que desejamos imprimir
    mostraLinha()
    print("{:^30}".format(msg))
    mostraLinha()


mensagem("OLÁ MUNDO!")
mensagem("PYTHON É BOM DEMAIS!")
