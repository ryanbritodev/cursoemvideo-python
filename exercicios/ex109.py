from modulos import moedas

p = float(input("Digite o preço: R$"))
print(f"A metade de {moedas.moedas(p)} é {moedas.metade(p, True)}")
print(f"O dobro de {moedas.moedas(p)} é {moedas.dobro(p, True)}")
print(f"Aumentando em 10%, temos {moedas.aumentar(p, 10, True)}")
print(f"Reduzindo 13%, temos {moedas.diminuir(p, 13, True)}")
