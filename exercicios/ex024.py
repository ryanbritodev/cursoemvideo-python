cidade = str(input("Digite o nome da sua cidade: "))
santoCidade = "SANTO" in (cidade.upper()).strip()[:5]

if santoCidade == True:
    print('Sua cidade tem "Santo" no começo do nome!')
else:
    print('Sua cidade não tem "Santo" no começo do nome!')
