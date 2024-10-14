def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um número
    :param n: O número a ser calculado.
    :param show: Mostrar ou não a conta (opcional).
    :return: O valor do fatorial de um número n.
    """
    fat = 1
    for i in range(n, 0, -1):
        fat *= i
    if show:
        conta = ""
        for l in range(n, 0, -1):
            if l == 1:
                conta += f"{l}"
            else:
                conta += f"{l} x "
        return f"{conta} = {fat}"
    else:
        return fat


print("-" * 30)
numero = int(input("Digite um número: "))

flag = str(input("Quer mostrar o cálculo? [S/N] ")).strip().upper()[0]
while flag not in "SN":
    print("Opção inválida! Tente novamente")
    flag = str(input("Quer mostrar o cálculo? [S/N] ")).strip().upper()[0]
if flag == "S":
    flag = True
else:
    flag = False

print(fatorial(numero, show=flag))
