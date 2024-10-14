def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}")

f1 = fatorial(6)
f2 = fatorial(7)
f3 = fatorial(8)

print(f"Os fatoriais são {f1}, {f2} e {f3}")
