num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print("RESULTADO:")
# Verificando quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# Verificando quem é o maior
maior = num2
if num1 > num3 and num1 > num2:
    maior = num1
if num3 > num2 and num3 > num1:
    maior = num3

print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))

"""if num1 > num2 and num1 > num3:
    print("Maior número: {}".format(num1))
elif num2 > num1 and num2 > num3:
    print("Maior número: {}".format(num2))
elif num3 > num1 and num3 > num2:
    print("Maior número: {}".format(num3))

if num1 == num2 and num1 > num3:
    print("Maior número: {}".format(num1))
elif num2 == num3 and num2 > num1:
    print("Maior número: {}".format(num2))
elif num1 == num3 and num1 > num2:
    print("Maior número: {}".format(num3))

if num1 < num2 and num1 < num3:
    print("Menor número: {}".format(num1))
elif num2 < num1 and num2 < num3:
    print("Menor número: {}".format(num2))
elif num3 < num1 and num3 < num2:
    print("Menor número: {}".format(num3))

if num1 == num2 and num1 < num3:
    print("Menor número: {}".format(num1))
elif num2 == num3 and num2 < num1:
    print("Menor número: {}".format(num2))
elif num3 == num1 and num1 < num2:
    print("Menor número: {}".format(num3))

if num1 == num3 == num2:
    print("Os números são iguais!")"""
