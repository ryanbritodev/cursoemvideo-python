from sys import exit
from datetime import date

print("""    _    _     ___ ____ _____  _    __  __ _____ _   _ _____ ___  
   / \  | |   |_ _/ ___|_   _|/ \  |  \/  | ____| \ | |_   _/ _ \ 
  / _ \ | |    | |\___ \ | | / _ \ | |\/| |  _| |  \| | | || | | |
 / ___ \| |___ | | ___) || |/ ___ \| |  | | |___| |\  | | || |_| |
/_/   \_\_____|___|____/ |_/_/   \_\_|  |_|_____|_| \_| |_| \___/ 
""")
print("""                       ⢰⣿⣿⣿⣆⠀⣀⣀⣤⣴⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⡀⠀⠀⠀⠀
                ⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡄⠀
                ⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
                ⠀⠀⠈⠛⠉⠁⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

print("=============== INFORMAÇÕES SOBRE O ALISTAMENTO MILITAR ===============\n")

print("""O alistamento militar no Brasil é obrigatório para todos os homens que completam 18 anos. Aqui estão algumas informações úteis sobre o processo:

1. Onde se alistar:
   - Você pode se alistar online pelo site do Exército Brasileiro: https://www.alistamento.eb.mil.br/.
   - Caso prefira, pode se dirigir a uma Junta de Serviço Militar (JSM) mais próxima de sua residência.

2. Documentos necessários:
   - Certidão de Nascimento ou Documento de Identidade (RG).
   - Comprovante de Residência.
   - Duas fotos 3x4 recentes.

3. Prazo para alistamento:
   - O período de alistamento vai de 1º de janeiro até 30 de junho do ano em que o cidadão completa 18 anos.

4. Consequências da não apresentação:
   - Se você não se alistar no prazo, estará em débito com o serviço militar e poderá enfrentar restrições como:
     - Impossibilidade de tirar passaporte.
     - Impossibilidade de ingressar no serviço público.
     - Impossibilidade de se matricular em instituições de ensino.

5. Procedimentos após o alistamento:
   - Após o alistamento, você passará por uma seleção geral e poderá ser designado para servir ou ser dispensado, conforme as necessidades das Forças Armadas.

Se você já passou do prazo para o alistamento, deve regularizar sua situação na Junta de Serviço Militar o quanto antes para evitar problemas futuros.
""")

print("Vamos descobrir se você deve ou não se alistar?")
sexo = str(input("Informe seu GÊNERO (masculino ou feminino): ").strip().lower())

if sexo == "feminino":
    exit("Pessoas do gênero feminino não precisam se alistar!")
elif sexo == "masculino":
    print(end="")
else:
    exit("Resposta inválida!")

anoNascimento = int(input("Informe seu ANO DE NASCIMENTO: ").strip())
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if 17 != idade < 18:
    print("Ainda não chegou a hora do seu alistamento!\nSeu alistamento será em {} (restam {} anos).".format(anoAtual + (18 - idade), (anoAtual + (18 - idade)) - anoAtual))
elif 17 == idade:
    print("Ainda não chegou a hora do seu alistamento!\nSeu alistamento será em {} (resta {} ano).".format(anoAtual + (18 - idade), (anoAtual + (18 - idade)) - anoAtual))
elif idade == 18:
    print("A hora de se alistar chegou!")
elif 19 != idade > 18:
    print("Você já deveria ter se alistado!\nSeu alistamento ocorreu em {} (já se passaram {} anos).".format((anoAtual - idade) + 18, anoAtual - ((anoAtual - idade) + 18)))
else:
    print("Você já deveria ter se alistado!\nSeu alistamento ocorreu em {} (já se passou {} ano).".format((anoAtual - idade) + 18, anoAtual - ((anoAtual - idade) + 18)))
