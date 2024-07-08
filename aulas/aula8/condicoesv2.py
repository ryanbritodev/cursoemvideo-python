cores = {"limpa": "\033[m",
         "vermelho": "\033[31m",
         "amarelo": "\033[33m",
         "pretoebranco": "\033[30;107m"}

nome = str(input("Qual é o seu nome? "))
if nome == "Ryan":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Ana":
    print("Seu nome é bem popular no Brasil")
elif nome in "Paula Cláudia Jéssica Juliana":
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal")
print("{}Tenha um bom dia, {}!{}".format(cores["amarelo"], nome, cores["limpa"]))
