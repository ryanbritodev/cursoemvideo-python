distanciaViagem = int(input("Digite a distância da viagem (em km): "))
distancia = 0

if distanciaViagem <= 200:
    print("Sua viagem é curta!")
    distanciaFinal = distancia + (distanciaViagem * 0.5)
else:
    print("Sua viagem é longa!")
    distanciaFinal = distancia + (distanciaViagem * 0.45)

print("Valor final da sua viagem: R${}".format(distanciaFinal))
