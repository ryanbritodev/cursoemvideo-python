# Tratamento de Erros e Exceções
# https://www.w3schools.com/python/python_ref_exceptions.asp
# Esse erro/exceção não está relacionado a síntaxe, e sim pela não declaração da variável "X", ocasionando no erro "NameError"

# Exemplos:
# print(x)

# Se digitarmos qualquer outra coisa, que não um número inteiro (como uma string), teremos uma exceção "ValueError", que se dá pelo erro de valor
n = int(input("Digite um número: "))
print(f"Você digitou o número {n}")

n2 = int(input("Digite um segundo número: "))
r = n / n2

# Se tentarmos dividir o valor por zero, teremos a exceção "ZeroDivisionError", que é o erro por divisão de um número por zero
print(f"O resultado é {r}")

# TypeError (Erro de Tipo, o que não acontece por exemplo em JavaScript e PHP)
# r = 2 / "2"

# IndexError ou KeyError (índice 3 está fora do range da lista, que vai até o índice 2)
lst = [3, 6, 4]
print(lst[3])

# import uteis
# Caso o arquivo não seja encontrado, ele irá chamar a exceção ModuleNotFoundError
