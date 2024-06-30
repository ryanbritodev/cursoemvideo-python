num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 1000
m = num // 1000 % 10000
print("Analisando o número {}...".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

'''
numero = str(input("Digite um número de 0 a 9999: "))


while True:
    if len(numero) > 4:
        print("O seu número é muito grande! Tente novamente")
        numero = str(input("Digite um número de 0 a 9999: "))
    elif len(numero) == 4:
        unidade = numero[3]
        dezena = numero[2]
        centena = numero[1]
        milhar = numero[0]
        print("""MILHAR: {}
CENTENA: {}
DEZENA: {}
UNIDADE: {}""".format(milhar, centena, dezena, unidade))
        break
    elif len(numero) == 3:
        unidade = numero[2]
        dezena = numero[1]
        centena = numero[0]
        print("""CENTENA: {}
DEZENA: {}
UNIDADE: {}""".format(centena, dezena, unidade))
        break
    elif len(numero) == 2:
        unidade = numero[1]
        dezena = numero[0]
        print("""DEZENA: {}
UNIDADE: {}""".format(dezena, unidade))
        break
    elif len(numero) == 1:
        unidade = numero[0]
        print("UNIDADE: {}".format(unidade))
        break
    elif len(numero) == 0:
        print("Vazio! Tente novamente")
        numero = str(input("Digite um número de 0 a 9999: "))
    else:
        break
'''