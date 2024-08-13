# DICIONÁRIOS
# Dicionários são coleções de dados que, ao contrário
# de listas, que são indexadas por valores numéricos,
# são indexadas por chaves literais (personalizáveis),
# como strings, por exemplo.

# Tuplas = ()
# Listas = []
# Dicionários = {}

# Exemplo de dicionário:
dicionario = dict()
dados = {"nome": "Pedro", "idade": 25}
print(dados["nome"]) # Pedro
print(dados["idade"]) # 25

print()

# Como posso criar outro elemento?
# Exemplo:
dados["sexo"] = "M"
print(dados)

# Como posso deletar um elemento?
# Exemplo:
del dados["idade"]
print(dados)

starWars = {"título": "Star Wars",
            "ano": 1977,
            "diretor": "George Lucas",
            "gênero": "Ficção Científica"}

avengers = {"título": "Avengers",
            "ano": 2012,
            "diretor": "Joss Whedon",
            "gênero": "Ação"}

matrix = {"título": "Matrix",
          "ano": 1999,
          "diretor": "Lana Wachowski",
          "gênero": "Ficção Científica"}

# O que são itens, chaves e valores de um dicionário?
# Exemplo:
# itens: título, Star Wars
# chaves: título
# valores: Star Wars

print()

# Como acessar itens, chaves e valores de um dicionário?
# Exemplo:
print(starWars.values()) # dict_values(['Star Wars', 1977, 'George Lucas', 'Ficção Científica'])
print(starWars.keys()) # dict_keys(['título', 'ano', 'diretor', 'gênero'])
print(starWars.items()) # dict_items([('título', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas'), ('gênero', 'Ficção Científica')])

print()

for chave, valor in starWars.items():
    print(f"O {chave} é {valor}")

locadora = []

locadora.append(starWars)
locadora.append(avengers)
locadora.append(matrix)

print()

print(locadora)
print(locadora[0]["título"])
print(locadora[1]["ano"])
