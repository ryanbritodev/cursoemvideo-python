nome = str(input("Digite o seu nome completo: "))

nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
primeiroNome = nome.split()[0]
nomeSeparado = nome.split()
nomeSemEspaco = "".join(nomeSeparado)
# nomeSemEspaco = len(nome) - nome.count(" ")))

print("""Analisando seu nome...
NOME COM TODAS AS LETRAS MAIÚSCULAS: {}
NOME COM TODAS AS LETRAS MINÚSCULAS: {}
QUANTIDADE DE LETRAS AO TODO: {}
SEU PRIMEIRO NOME: {}
QUANTIDADE DE LETRAS NO PRIMEIRO NOME: {}""".format(nomeMaiusculo, nomeMinusculo, len(nomeSemEspaco), primeiroNome.capitalize(), len(primeiroNome)))
