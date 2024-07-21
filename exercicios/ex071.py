print("""  ____      _                                 
 / ___|__ _(_)_  ____ _                       
| |   / _` | \ \/ / _` |                      
| |__| (_| | |>  < (_| |                      
 \____\__,_|_/_/\_\__,_//\        _           
| ____| | ___| |_ _ __|/_\| _ __ (_) ___ ___  
|  _| | |/ _ \ __| '__/ _ \| '_ \| |/ __/ _ \ 
| |___| |  __/ |_| | | (_) | | | | | (_| (_) |
|_____|_|\___|\__|_|  \___/|_| |_|_|\___\___/ """)

print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡤⡄⠒⠊⠉⢀⣀⢨⠷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡇⠈⢹⣩⢟⣜⣐⡵⡿⢇⠀⠀⠀⠀⠀⠀
⠀⠀⡠⠖⠊⠉⠀⠀⠈⠻⢅⠀⠀⠀⠀⠀⠈⠒⠠⢀⠀⠀
⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⠀⠀⠀⠀⣀⣀⣼⠂
⢰⠃⠀⠀⠀⡀⡀⠀⠀⠀⠀⠀⠀⠈⢷⡲⡺⣩⡤⢊⠌⡇
⠸⡆⠀⠀⡞⠀⡇⠀⢰⣓⢢⣄⠀⠀⢸⣞⡞⢉⠔⡡⢊⣷
⠀⢣⠀⠀⠹⡄⡇⠀⢸⣂⡡⢖⠳⣄⢸⢋⠔⡡⢊⣰⠠⠋
⠀⠀⢣⡀⠀⠈⠁⠀⠸⣗⠾⣙⣭⡾⢿⡶⢏⠁⠀⠀⠀⠀
⠀⠀⠀⠳⡀⠀⠀⠀⠀⠻⣽⠊⣡⠞⢉⢔⠝⣑⢄⠀⠀⠀
⠀⠀⠀⢀⣹⣆⠀⠀⠀⠀⠈⠳⣤⢊⠔⡡⠊⢁⡤⠓⠄⠀
⠀⡶⡿⣋⣵⢟⣧⠀⠀⠀⠀⠀⠈⢧⡊⣀⠔⡩⠐⣀⠙⡄
⠸⡇⢹⣋⠕⡫⠘⡇⠀⣄⠀⠀⠀⠀⢻⡕⢁⠤⠊⢁⡀⡇
⠀⡇⠀⠳⣵⢊⢽⡇⠀⡏⢳⡀⠀⠀⠀⣟⣡⠴⠚⡉⠠⡇
⠀⠘⢆⡀⠈⠉⠉⠀⠀⣧⣼⡗⠀⠀⠀⣹⠐⣈⠠⠤⣰⠀
⠀⠀⠀⠙⠦⡀⠀⠀⠀⠉⠉⠀⠀⠀⢀⡯⠥⣒⣂⡱⠃⠀
⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⢀⣞⣉⠭⠴⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡆⠀⡶⣶⠶⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n""")

cedulas1 = cedulas10 = cedulas20 = cedulas50 = 0

valor = int(input("Qual valor você deseja sacar? R$"))

while valor < 1:
    print("\nDigite um valor válido\n")
    valor = int(input("Qual valor você deseja sacar? R$"))

if valor >= 50:
    cedulas50 = valor // 50
    valor %= 50

"""
EXEMPLO DE USO DO OPERADOR %=
valor = 78
cedulas50 = valor // 50  # Quantidade de cédulas de 50
restante = valor % 50    # Resto após retirar as cédulas de 50
78 % 50 = 78 − (50 × 1) = 78 − 50 =28
print(cedulas50)  # Saída: 1
print(restante)   # Saída: 28
"""

if valor >= 20:
    cedulas20 = valor // 20
    valor %= 20
if valor >= 10:
    cedulas10 = valor // 10
    valor %= 10
if valor >= 1:
    cedulas1 = valor // 1
    valor %= 1

if cedulas50 > 0:
    print(f"Total de cédulas de R$50: {int(cedulas50)}")
if cedulas20 > 0:
    print(f"Total de cédulas de R$20: {int(cedulas20)}")
if cedulas10 > 0:
    print(f"Total de cédulas de R$10: {int(cedulas10)}")
if cedulas1 > 0:
    print(f"Total de cédulas de R$1: {int(cedulas1)}")

print("Volte sempre ao Caixa Eletrõnico! Muito obrigado!")
