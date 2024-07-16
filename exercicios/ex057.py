print(""" __  __                      _ _                           
|  \/  | __ _ ___  ___ _   _| (_)_ __   ___                
| |\/| |/ _` / __|/ __| | | | | | '_ \ / _ \               
| |  | | (_| \__ \ (__| |_| | | | | | | (_) |              
|_|  |_|\__,_|___/\___|\__,_|_|_|_| |_|\___/           ___ 
  ___  _   _  |  ___|__ _ __ ___ (_)_ __ (_)_ __   ___|__ |
 / _ \| | | | | |_ / _ \ '_ ` _ \| | '_ \| | '_ \ / _ \ / /
| (_) | |_| | |  _|  __/ | | | | | | | | | | | | | (_) |_| 
 \___/ \__,_| |_|  \___|_| |_| |_|_|_| |_|_|_| |_|\___/(_) \n""")

sexo = (str(input("Informe seu sexo [M/F]: ")).strip().upper()).replace(" ", "")[0]

while sexo not in "MmFf":
    sexo = str(input("{}Dados inválidos!{}\nPor favor, informe seu sexo: ".format("\033[1;31m", "\033[m"))).strip().upper().replace(" ", "")[0]
print("{}Sexo {} registrado com sucesso!{}".format("\033[1;32m", sexo, "\033[m"))
print("Obrigado pela informação!")
