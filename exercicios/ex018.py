from math import radians, sin, cos, tan

angulo = int(input("Digite o valor de um ângulo qualquer: "))


anguloRadianos = radians(angulo)

seno = sin(anguloRadianos)
cosseno = cos(anguloRadianos)
tangente = tan(anguloRadianos)

print("SENO, COSSENO E TANGENTE DE UM ÂNGULO DE {}°".format(angulo))
print("SENO: {0}°\nCOSSENO: {1}°\nTANGENTE: {2}°".format(seno, cosseno, tangente))
