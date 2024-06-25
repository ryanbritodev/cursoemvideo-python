preco = float(input("Qual é o preço do produto? R$"))
precoNovo = preco - (preco * 5 / 100)
print("O produto que custava R${:.2f}, agora com 5% de desconto terá o valor de R${:.2f}!".format(preco, precoNovo))
