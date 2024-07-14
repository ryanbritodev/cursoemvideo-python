print("""  ___                                               
 / _ \ _   _  ___ _ __ ___    _ __   ___  ___  __ _ 
| | | | | | |/ _ \ '_ ` _ \  | '_ \ / _ \/ __|/ _` |
| |_| | |_| |  __/ | | | | | | |_) |  __/\__ \ (_| |
 \__\_||__,_|\___|_| |_|_|_| | .__/ \___||___/\__,_|
 _ __ ___   __ _(_)__|__ \   |_|                    
| '_ ` _ \ / _` | / __|/ /                          
| | | | | | (_| | \__ \_|                           
|_| |_| |_|\__,_|_|___(_)                           \n""")

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: ".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

if maior == menor:
    print("\nO maior e menor peso lidos foram iguais, sendo de {}kg".format(maior))
else:
    print("\nO maior peso lido foi de {}kg".format(maior))
    print("O menor peso lido foi de {}kg".format(menor))

# Solução que eu cheguei ↓

"""lista = list()

for i in range(1, 6):
    pessoa = float(input("INFORME O PESO DA {} PESSOA: ".format(i)))
    lista.append(pessoa)
lista.sort()
print("\nMAIOR PESO: {}kg\nMENOR PESO: {}kg".format(lista[4], lista[0]))"""
