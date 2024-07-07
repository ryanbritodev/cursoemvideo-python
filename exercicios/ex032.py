from datetime import date

print("=-"*15, "ANO BISSEXTO", "-="*15)
print('Digite o número de um ano qualquer ou digite "0" para digitar o ano atual')
ano = int(input("Informe o ano: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")
