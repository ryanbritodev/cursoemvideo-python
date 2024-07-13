from math import pow

print("""  ____   __  _     ____ _   _ _     ___  
 / ___| /_/ | |   / ___| | | | |   / _ \ 
| |     /_\ | |  | |   | | | | |  | | | |
| |___ / _ \| |__| |___| |_| | |__| |_| |
 \____/_/ \_\_____\____|\___/|_____\___/ 
       ____   ___    ___ __  __  ____    
      |  _ \ / _ \  |_ _|  \/  |/ ___|   
      | | | | | | |  | || |\/| | |       
      | |_| | |_| |  | || |  | | |___    
      |____/ \___/  |___|_|  |_|\____|   
""")

peso = float(input("Informe seu PESO (em quilogramas): "))
altura = float(input("Informe sua ALTURA (em metros): "))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print("\nVocê está ABAIXO DO PESO!")
elif 18.5 <= imc < 25:
    print("\nVocê está no PESO IDEAL! Parabéns!")
elif 25 <= imc < 30:
    print("\nVocê está com SOBREPESO!")
elif 30 <= imc < 40:
    print("\nVocê está OBESO!")
elif imc >= 40:
    print("\nVocê está com OBESIDADE MÓRBIDA! Cuidado!")
