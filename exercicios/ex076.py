print(""" _____     _          _             _      
|_   _|_ _| |__   ___| | __ _    __| | ___ 
  | |/ _` | '_ \ / _ \ |/ _` |  / _` |/ _ |
  | | (_| | |_) |  __/ | (_| | | (_| |  __/
 _|_|\__,_|_.__/ \___|_|\__,_|  \__,_|\___|
|  _ \ _ __ ___  ___ ___  ___              
| |_) | '__/ _ \/ __/ _ \/ __|             
|  __/| | |  __/ (_| (_) \__ \             
|_|   |_|  \___|\___\___/|___/             
                 )_)                       """)

produtos = ("Lápis", 1.5, "Borracha", 2, "Caderno", 15.9, "Estojo",
            25, "Transferidor", 4.2, "Compasso", 9.99, "Mochila",
            120.32, "Canetas", 22.3, "Livro", 34.9)

nome = 0
valor = 1

quantidade = len(produtos) // 2 + 1

print("=" * 40)
print("{:^40}".format("LISTAGEM DE PREÇOS"))
print("=" * 40)

for i in range(1, quantidade):
    print(f"{produtos[nome]}{'.' * (40 - len(produtos[nome]) - 2 - len(str(produtos[valor])))}R${produtos[valor]}")
    nome += 2
    valor += 2

print("=" * 40)
