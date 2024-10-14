from datetime import date

anoAtual = date.today().year


def votar(ano=anoAtual - 120):
    n = anoAtual - ano
    if n < 18:
        return "NÃO VOTA"
    elif n > 65:
        return "VOTO OPCIONAL"
    else:
        return "VOTO OBRIGATÓRIO"


print("=-" * 20)
anoNascimento = int(input("Em que ano você nasceu? "))
print(f"Com {anoAtual - anoNascimento} anos: {votar(anoNascimento)}.")
