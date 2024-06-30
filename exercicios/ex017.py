from math import pow, sqrt, hypot

catetoOposto = float(input("Qual o comprimento (em cm) do cateto oposto do triângulo retângulo? "))
catetoAdjacente = float(input("Qual o comprimento (em cm) do cateto adjacente do triângulo retângulo? "))

"""pitagoras = pow(catetoOposto, 2) + pow(catetoAdjacente, 2)

resultado = sqrt(pitagoras)"""

hipotenusa = hypot(catetoOposto, catetoAdjacente)

print("O valor da hipotenusa do triângulo retângulo com o cateto oposto de comprimento {0}cm e do cateto adjacente de comprimento {1}cm é de {2:.2f}cm".format(catetoOposto, catetoAdjacente, hipotenusa))
