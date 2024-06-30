nome = str(input("Qual seu nome? "))
nomeComSilva = "SILVA" in nome.upper().strip()

if nomeComSilva == True:
    print('Você tem "Silva" no nome!')
else:
    print('Você não tem "Silva" no nome!')
