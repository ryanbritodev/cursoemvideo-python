salario = float(input("Qual é o salário do funcionário? R$"))
aumentoSalario = salario + (salario * 15 / 100)
print("Um funcionário que ganhava R${:.2F}, com seu novo aumento de 15%, terá um novo salário de R${:.2f}!".format(salario, aumentoSalario))
