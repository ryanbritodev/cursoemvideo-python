from datetime import datetime

dados = dict()
dados["nome"] = str(input("Nome: ")).strip().title()
nasc = int(input("Ano de Nascimento: "))
dados["idade"] = datetime.today().year - nasc
dados["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))

if dados["ctps"] != 0:
    dados["contratacao"] = int(input("Ano de Contratação: "))
    dados["salario"] = float(input("Salário: R$"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 35) - datetime.today().year)
print("-=" * 35)
for k, v in dados.items():
    print(f"  - {k} tem o valor {v}")

# ano = date.today().year
#
# pessoa = {}
#
# nome = str(input("Nome: ")).strip().title()
# anoNascimento = int(input("Ano de Nascimento: "))
# carteira = int(input("Carteira de Trabalho (0 não tem): "))
# anoContratacao = int(input("Ano de Contratação: "))
# salario = float(input("Salário: R$"))
#
# pessoa["Nome"] = nome
# pessoa["Idade"] = ano - anoNascimento
# pessoa["CTPS"] = carteira
# pessoa["Contratação"] = anoContratacao
# pessoa["Salário"] = salario
# pessoa["Aposentadoria"] = (anoNascimento + 65) - (ano - anoNascimento)
