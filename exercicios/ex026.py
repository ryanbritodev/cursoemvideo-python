frase = str(input("Digite uma frase: "))
quantidadeA = frase.upper().count("A")
primeiroA = frase.strip().upper().find("A") + 1
ultimoA = frase.strip().upper().rfind("A") + 1

print('Quantidade de vezes que a letra "A" aparece na sua frase: {}'.format(quantidadeA))
print('Índice da primeira ocorrência da letra "A": {}'.format(primeiroA))
print('Índice da última ocorrência da letra "A": {}'.format(ultimoA))
