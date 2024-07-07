salario = float(input("Digite o seu salário: "))

aumentoSalario = ""
aumento = ""

if salario > 1250:
    aumentoSalario = salario + (salario * 0.1)
    aumento = salario * 0.1
elif salario <= 1250:
    aumentoSalario = salario + (salario * 0.15)
    aumento = salario * 0.15

print("O seu novo salário, com um aumento de R${:.2f}, é de R${:.2f}!".format(aumento, aumentoSalario))
