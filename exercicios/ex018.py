from math import radians, sin, cos, tan

angulo = int(input("Digite o valor de um ângulo qualquer: "))

anguloRadianos = radians(angulo)

seno = sin(anguloRadianos)
cosseno = cos(anguloRadianos)
tangente = tan(anguloRadianos)

print("SENO, COSSENO E TANGENTE DE UM ÂNGULO DE {}°".format(angulo))
print("SENO: {0:.2f}°\nCOSSENO: {1:.2f}°\nTANGENTE: {2:.2f}°".format(seno, cosseno, tangente))
