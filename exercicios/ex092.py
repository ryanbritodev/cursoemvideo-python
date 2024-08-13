from datetime import date

ano = date.today().year

pessoa = {}

nome = str(input("Nome: ")).strip().title()
anoNascimento = int(input("Ano de Nascimento: "))
carteira = int(input("Carteira de Trabalho (0 não tem): "))
anoContratacao = int(input("Ano de Contratação: "))
salario = float(input("Salário: R$"))

pessoa["Nome"] = nome
pessoa["Idade"] = ano - anoNascimento
pessoa["CTPS"] = carteira
pessoa["Contratação"] = anoContratacao
pessoa["Salário"] = salario
pessoa["Aposentadoria"] = (anoNascimento + 65) - (ano - anoNascimento)
