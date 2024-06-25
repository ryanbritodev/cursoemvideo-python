grausCelsius = float(input("Qual é a temperatura em graus celsius (C°) a ser convertida? "))
grausFahrenheit = grausCelsius * 9/5 + 32
grausKelvin = grausCelsius + 273.15

print("A temperatura de {}°C equivale a {}°F e a {}°K".format(grausCelsius, grausFahrenheit, grausKelvin))
