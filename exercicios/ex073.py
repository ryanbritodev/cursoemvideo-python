print(""" ____                _ _      _      /\/|                
| __ ) _ __ __ _ ___(_) | ___(_)_ __|/\/_  ___           
|  _ \| '__/ _` / __| | |/ _ \ | '__/ _` |/ _ \          
| |_) | | | (_| \__ \ | |  __/ | | | (_| | (_) |         
|____/|_|__\__,_|___/_|_|\___|_|_|  \__,_|\___/          
/ ___|  /_/ _ __(_) ___     / \                          
\___ \ / _ \ '__| |/ _ \   / _ \                         
 ___) |  __/ |  | |  __/  / ___ \                        
|____/_\___|_|  |_|\___| /_/___\_\         _         __  
 / / ___|___  _ __ ___   |_   _|   _ _ __ | | __ _ __\ \ 
| | |   / _ \| '_ ` _ \    | || | | | '_ \| |/ _` / __| |
| | |__| (_) | | | | | |   | || |_| | |_) | | (_| \__ \ |
| |\____\___/|_| |_| |_|   |_| \__,_| .__/|_|\__,_|___/ |
 \_\                                |_|              /_/ """)

print("""                     ___
 o__        o__     |   ||
/|          /\      |   |X|
/ > o        <\     |   |XX|\n""")

brasileirao = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Athletico-PR", "Red Bull Bragantino", "Atlético-MG", "Vasco da Gama", "Juventude", "Internacional", "Corinthians", "Criciúma", "Cuiabá", "EC Vitória", "Grêmio", "Fluminense", "Atlético-GO")

print("{:-^50}".format(" TABELA BRASILEIRÃO SÉRIE A "))

print(f"Primeiros 5 colocados (G5): {brasileirao[0:5]}")
print(f"Últimos 4 colocados (Z4): {brasileirao[-4:]}")
print(f"Equipes em ordem alfabética: {sorted(brasileirao)}")
time = str(input("Digite o nome de um time para ver sua posição: "))
while time not in brasileirao:
    print("Opção Inválida!")
    time = str(input("Digite o nome de um time para ver sua posição: "))
print(f"Posição do {time} na tabela: {brasileirao.index(time) + 1}°")
