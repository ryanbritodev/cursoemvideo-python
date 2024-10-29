import requests
import urllib3  # Módulo para desabilitar os avisos de Certificado

urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

url = "https://www.pudim.com.br/"

try:
    resposta = requests.get(url, verify=False)  # Sem verificar o certificado SSL, que é um certificado necessário pra estabelecer uma conexão HTTPS segura
    if resposta.ok:
        print(f"{"\033[1;32m"}Consegui acessar o site Pudim com sucesso!{"\033[m"}")
    else:
        print(f"{"\033[1;31m"}O site Pudim foi acessado mas não está disponível no momento! :({"\033[m"}")
except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as erro:
    print(f"{"\033[1;31m"}O site Pudim não está acessível no momento! :(\nErro: {erro}{"\033[m"}")
except Exception as erro:
    print(f"{"\033[1;31m"}Erro Desconhecido! :(\nErro: {erro}{"\033[m"}")
