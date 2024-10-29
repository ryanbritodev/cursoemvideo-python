# Os blocos de Try e Except podem ter vários Excepts ao mesmo tempo, enquanto os blocos Else e Finally são opcionais

try:
    # Operação
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    # Falhou
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")
except Exception as erro:
    print(f"Tivemos um problema! :(\nErro: {erro.__cause__}")
else:
    # Deu Certo
    print(f"O resultado é {r:.1f}")
finally:
    # Certo/Falha
    # Acontece independente se der certo ou errado
    print("Volte sempre! Muito Obrigado!")
