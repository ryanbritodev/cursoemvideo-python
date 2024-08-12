teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = "Maria"
teste[1] = 22
galera.append(teste)
print(galera)
# Resultado: [['Maria', 22], ['Maria', 22]]
# Porque isso acontece?
# Porque a lista teste é uma lista mutável, ou seja, quando alteramos
# o valor de teste, alteramos o valor de galera também, pois galera
# é uma lista de listas, e a lista teste é uma lista que foi adicionada
# a galera. Para corrigir isso, podemos usar o método copy() para
# copiar o valor de teste para galera.
pessoal = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(pessoal)
print(pessoal[0]) # Dados do João
print(pessoal[0][0]) # Nome do João
print(pessoal[2][1]) # Idade do Joaquim
for p in pessoal:
    print(f"{p[0]} tem {p[1]} anos de idade.")
