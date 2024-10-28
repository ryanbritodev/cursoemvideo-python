def notas(* valores, situacao=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param valores: Uma ou mais notas dos alunos (aceita várias).
    :param situacao: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dic = dict()
    total = soma = maior = 0
    menor = valores[0]
    for valor in valores:
        soma += valor
        total += 1
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    media = soma / total
    dic["total"] = total
    dic["maior"] = maior
    dic["menor"] = menor
    dic["media"] = media
    sit = ""
    if situacao:
        if media >= 7:
            sit = "BOA"
        elif 6 <= media < 7:
            sit = "RAZOÁVEL"
        elif media < 6:
            sit = "RUIM"
        dic["situacao"] = sit
        return dic
    else:
        return dic


# Programa Principal
# help(notas)
resposta = notas(10, 2.5, 5.5, 6.5, situacao=True)
print(resposta)
