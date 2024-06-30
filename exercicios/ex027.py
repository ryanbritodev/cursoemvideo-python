nome = str(input("Digite seu nome completo: ")).strip()
primeiroNome = nome.split()[0]
listaNome = nome.split()
indiceUltimoNome = len(listaNome) - 1

print("Muito prazer em te conhecer!")
print("Primeiro nome: {}\nÚltimo nome: {}".format(primeiroNome, listaNome[indiceUltimoNome]))
