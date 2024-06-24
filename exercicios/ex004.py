valor = input("Digite algo: ")
print("O tipo primitivo desse valor é {}".format(type(valor)))
print("Só tem espaços? ", valor.isspace())
print("É um número? ", valor.isnumeric()) # Mesmo sendo uma string, ele pode ser convertido em um número
print("É alfabético? ", valor.isalpha())
print("É alfanumérico? ", valor.isalnum())
print("Está em maiúsculas? ", valor.isupper())
print("Está em minúsculas? ", valor.islower())
print("Está capitalizada? ", valor.istitle())
