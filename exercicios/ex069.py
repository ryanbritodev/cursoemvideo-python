print("""  ____          _           _             
 / ___|__ _  __| | __ _ ___| |_ _ __ ___  
| |   / _` |/ _` |/ _` / __| __| '__/ _ \ 
| |__| (_| | (_| | (_| \__ \ |_| | | (_) |
 \____\__,_|\__,_|\__,_|___/\__|_|  \___/ """)

print("\nOlá! Vamos realizar seu cadastro hoje?\n")

contMulheres = contHomens = contIdade = sexo = flag = 0

while True:
    idade = int(input("Qual sua idade? "))
    sexo = str(input("Qual seu sexo? [M/F] ").replace(" ", "").upper())
    while sexo != "M" and sexo != "F":
        sexo = str(input("Qual seu sexo? [M/F] ").replace(" ", "").upper())
    if idade > 18:
        contIdade += 1
    if sexo == "M":
        contHomens += 1
    if sexo == "F" and idade < 20:
        contMulheres += 1
    flag = str(input("Quer continuar os cadastros? [S/N] ").replace(" ", "").upper())
    while flag != "S" and flag != "N":
        flag = str(input("Quer continuar os cadastros? [S/N] ").replace(" ", "").upper())
    if flag == "N":
        print("\n======== PROGRAMA ENCERRADO ==========")
        break
    else:
        continue
print(f"Total de pessoas com mais de de 18 anos: {contIdade}")
print(f"Ao todo temos {contHomens} homens cadastrados")
print(f"E temos {contMulheres} mulheres com menos de 20 anos")
