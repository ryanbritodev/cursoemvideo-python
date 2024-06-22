valor = input("Digite algo: ")

print('''
==== TABELA DO RESULTADO ====
True .................... Sim
False ................... Não
<class ''> ............. Tipo
=============================
''')

print("Tipo do valor: RESULTADO = {}".format(type(valor)))
print("É somente numérico? RESULTADO = {}".format(valor.isnumeric()))
print("É somente string? RESULTADO = {}".format(valor.isalpha()))
print("É string, númerico ou os dois? RESULTADO = {}".format(valor.isalnum()))
print("Tem somente maiúsculos? RESULTADO = {}".format(valor.isupper()))
