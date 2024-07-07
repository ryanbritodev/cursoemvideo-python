print("-" * 20, "CONTROLE DE VELOCIDADE", "-" * 20)
velocidade = int(input("Digite a velocidade do veículo ao passar no radar (km/h): "))
velocidadeExcedida = velocidade - 80

if velocidade > 80:
    print("Que pena! Por ter ultrapassado o limite de 80km/h da via\nem {}km/h, você foi multado. O valor da multa será de R${}".format(velocidadeExcedida, velocidadeExcedida * 7))
else:
    print("Ufa! Você não foi multado")
