n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

soma = n1 + n2
sub = n1 - n2
div = n1 / n2
mult = n1 * n2
divInt = n1 // n2
exp = n1 ** n2

print("A soma vale {0}, a subtração vale {1}, o produto da multiplicação é {2} e a divisão é {3:.2f}".format(soma, sub, mult, div), end=" ")
print("Divisão inteira é igual a {0} e a exponenciação {1}".format(divInt, exp))
