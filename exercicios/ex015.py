dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))

diariaCarro = dias * 60
valorKmRodado = 0.15 * km

total = diariaCarro + valorKmRodado

print("Com {} dias alugados e {:.0f}km rodados, o total a pagar é de R${:.2f}".format(dias, km, total))
