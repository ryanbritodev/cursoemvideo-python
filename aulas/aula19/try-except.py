# Os blocos de Try e Except podem ter vários Excepts ao mesmo tempo, enquanto os blocos Else e Finally são opcionais

try:
    # Operação
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:
    # Falhou
    print("Infelizmente tivemos um problema :(")
    print(f"Problema: {erro}")
    print(f"Classe do Erro: {erro.__class__}")
else:
    # Deu Certo
    print(f"O resultado é {r:.1f}")
finally:
    # Certo/Falha
    # Acontece independente se der certo ou errado
    print("Volte sempre! Muito Obrigado!")
