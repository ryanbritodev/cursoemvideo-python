dinheiroCarteira = float(input("Quantos reais você tem na carteira? R$"))
valorDolar = dinheiroCarteira / 5.39
valorEuro = dinheiroCarteira / 5.79
valorPeso = dinheiroCarteira / 0.0059
valorIenes = dinheiroCarteira / 0.034
print("Com R${0} você pode comprar U${1:.2f}, €{2:.2f}, AR${3:.2f} e ¥{4:.2f}!".format(dinheiroCarteira, valorDolar, valorEuro, valorPeso, valorIenes))
