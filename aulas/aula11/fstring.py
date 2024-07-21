nome = "José"
idade = 33
salario = 987.3
print(f"O {nome} tem {idade} anos.") # Python 3.6+
print("O {} tem {} anos.".format(nome, idade)) # Python 3
print("O %s tem %d anos." % (nome, idade)) # Python 2
print(f"O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}")
# %s = string
# %d = número inteiro
