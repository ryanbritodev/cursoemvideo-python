from modulos import leitura

cores = {
    "normal": "\033[m",
    "azul": "\033[0;0;36m",
    "amarelo": "\033[0;0;33m"
}

menu = f"""----------------------------------
          MENU PRINCIPAL
----------------------------------
{cores["amarelo"]}1{cores["normal"]} - {cores["azul"]}Ver Pessoas Cadastradas{cores["normal"]}
{cores["amarelo"]}2{cores["normal"]} - {cores["azul"]}Cadastrar Nova Pessoa{cores["normal"]}
{cores["amarelo"]}3{cores["normal"]} - {cores["azul"]}Sair do Sistema{cores["normal"]} 
----------------------------------"""

while True:
    print(menu)
    opcao = leitura.leiaInt(f"{cores["amarelo"]}Sua Opção: {cores["normal"]}")
    try:
        arquivo = open("ex115.txt")
        if opcao == 1:
            leitura.lerArquivo()
        elif opcao == 2:
            leitura.cadastroArquivo()
        elif opcao == 3:
            leitura.sairPrograma()
    except FileNotFoundError:
        if opcao == 1:
            leitura.criarArquivo()
            leitura.lerArquivo()
        elif opcao == 2:
            leitura.criarArquivo()
            leitura.cadastroArquivo()
        elif opcao == 3:
            leitura.sairPrograma()
