def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def leiaDinheiro(pergunta):
    valor = str(input(pergunta)).replace(",", ".")
    while not valor.strip().isnumeric() and not isfloat(valor):
        print(f'\033[1;31mERRO: "{valor.strip()}" é um preço inválido!\033[m')
        valor = str(input(pergunta))
    return float(valor)
