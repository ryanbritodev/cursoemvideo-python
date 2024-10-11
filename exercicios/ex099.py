from time import sleep


def maior(*valores):
    print("-=" * 30)
    print("Analisando os valores passados...")
    for valor in valores:
        print(valor, end=" ")
        sleep(0.25)
    print(f"\nForam informados {len(valores)} valores ao todo.")
    print(f"O maior valor informado foi {max(valores)}.")


maior(1, 5, 6, 3, 10, 9, 4)
