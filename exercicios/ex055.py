print("""  ___                                               
 / _ \ _   _  ___ _ __ ___    _ __   ___  ___  __ _ 
| | | | | | |/ _ \ '_ ` _ \  | '_ \ / _ \/ __|/ _` |
| |_| | |_| |  __/ | | | | | | |_) |  __/\__ \ (_| |
 \__\_||__,_|\___|_| |_|_|_| | .__/ \___||___/\__,_|
 _ __ ___   __ _(_)__|__ \   |_|                    
| '_ ` _ \ / _` | / __|/ /                          
| | | | | | (_| | \__ \_|                           
|_| |_| |_|\__,_|_|___(_)                           \n""")

lista = list()

for i in range(1, 6):
    pessoa = float(input("INFORME O SEU PESO: "))
    lista.append(pessoa)
lista.sort()
print("\nMAIOR PESO: {}\nMENOR PESO: {}".format(lista[4], lista[0]))
