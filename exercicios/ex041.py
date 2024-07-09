from datetime import date

print("""  ____    _  _____ _____ ____  ___  ____  ___    _    
 / ___|  / \|_   _| ____/ ___|/ _ \|  _ \|_ _|  / \   
| |     / _ \ | | |  _|| |  _| | | | |_) || |  / _ \  
| |___ / ___ \| | | |__| |_| | |_| |  _ < | | / ___ \ 
 \____/_/   \_\_| |_____\____|\___/|_| \_\___/_/   \_|
 _   _    _  _____  _    ____  /\/| ___               
| \ | |  / \|_   _|/ \  / ___||/\/ / _ \              
|  \| | / _ \ | | / _ \| |     /_\| | | |             
| |\  |/ ___ \| |/ ___ \ |___ / _ \ |_| |             
|_| \_/_/   \_\_/_/   \_\____/_/ \_\___/              
                          )_)                         
""")

anoNascimento = int(input("Informe o ANO DE NASCIMENTO do atleta: "))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print("O atleta pertence a categoria MIRIM!")
elif 9 < idade <= 14:
    print("O atleta pertence a categoria INFANTIL!")
elif 14 < idade <= 19:
    print("O atleta pertence a categoria JÚNIOR!")
elif 19 < idade <= 20:
    print("O atleta pertence a categoria SÊNIOR!")
elif idade > 20:
    print("O atleta pertence a categoria MASTER!")
