distanciaMetro = float(input("Digite a distância em metros a ser convertida: "))

distanciaMilimetro = distanciaMetro * 1000
distanciaCentimetro = distanciaMetro * 100
distanciaDecimetro = distanciaMetro * 10
distanciaDecametro = distanciaMetro * 0.1
distanciaHectometro = distanciaMetro * 0.01
distanciaQuilometro = distanciaMetro * 0.001

print("Distância em milímetros: {1}mm \nDistância em centímetros: {0}cm \nDistãncia de decímetros: {2}dm \nDistância em decâmetros: {3}dam \nDistância em hectômetros: {4}hm \nDistãncia em quilômetros: {5}km".format(distanciaCentimetro, distanciaMilimetro, distanciaDecimetro, distanciaDecametro, distanciaHectometro, distanciaQuilometro))
