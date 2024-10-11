def escreva(texto):
    tamanhoLinha = len(texto) + 2
    print("~" * tamanhoLinha)
    print(f"{texto:^{tamanhoLinha}}")
    print("~" * tamanhoLinha)


escreva("Gustavo Guanabara")
escreva("Curso de Python no Youtube")
escreva("Curso em Vídeo")
