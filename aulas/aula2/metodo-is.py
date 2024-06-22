valor = input("Digite algo: ")

print("É número? {}".format(valor.isnumeric()))
print("É string? {}".format(valor.isalpha()))
print("É string ou número? {}".format(valor.isalnum()))
print("É todo maiúsculo? {}".format(valor.isupper()))
