<<<<<<< HEAD
import json

=======
>>>>>>> 6b2aef8e10357f4ff86d2471dfe01288fb0cf736
print(""" _     ___ ____ _____  _    ____    ______   _______ _   _  ___  _   _  
| |   |_ _/ ___|_   _|/ \  / ___|  |  _ \ \ / /_   _| | | |/ _ \| \ | | 
| |    | |\___ \ | | / _ \ \___ \  | |_) \ V /  | | | |_| | | | |  \| | 
| |___ | | ___) || |/ ___ \ ___) | |  __/ | |   | | |  _  | |_| | |\  | 
|_____|___|____/ |_/_/   \_\____/  |_|    |_|  _|_| |_| |_|\___/|_| \_| 
|  \/  | __ _(_) ___  _ __    ___  _   _  |  \/  | ___ _ __   ___  _ __ 
| |\/| |/ _` | |/ _ \| '__|  / _ \| | | | | |\/| |/ _ \ '_ \ / _ \| '__|
| |  | | (_| | | (_) | |    | (_) | |_| | | |  | |  __/ | | | (_) | |   
|_|  |_|\__,_|_|\___/|_|     \___/ \__,_| |_|  |_|\___|_| |_|\___/|_|   \n""")

valores = []
maiores = []
menores = []

for cont in range(1, 6):
    valores.append(int(input(f"Digite o {cont}° valor: ")))

print("\nVocê digitou os valores ", end="")
for c, v in enumerate(valores):
    if valores[c] == max(valores):
        maiores.append(c)
    if valores[c] == min(valores):
        menores.append(c)
print(valores)

print(f"O maior valor digitado foi {max(valores)} nas posições {maiores}")
print(f"O menor valor digitado foi {min(valores)} nas posições {menores}")
