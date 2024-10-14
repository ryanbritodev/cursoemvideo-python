# Escopo de Variáveis

# Função Teste

def teste():
    x = 8
    # Variável LOCAL
    print(f"Na função teste, x vale {x}")
    print(f"Na função teste, n vale {n}")


# Programa principal
n = 2
# Variável GLOBAL
print(f"No programa principal, n vale {n}")
teste()

# A variável X só existe no programa principal, e por isso, vai dar o um NameError, dizendo que X não foi definido, como se não existisse mesmo
# print(f"No programa principal, x vale {x}")
