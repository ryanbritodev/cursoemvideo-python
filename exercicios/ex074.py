print(""" _   _   __                                             
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___               
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|              
| |\  | |_| | | | | | |  __/ | | (_) \__ \              
|_|_\_|\__,_|_| |_| |_|\_//\_|  \___/|___/              
|  _ \ __ _ _ __   __| ||/_\| _ __ ___ (_) ___ ___  ___ 
| |_) / _` | '_ \ / _` |/ _ \| '_ ` _ \| |/ __/ _ \/ __|
|  _ < (_| | | | | (_| | (_) | | | | | | | (_| (_) \__ |
|_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|_|\___\___/|___/""")

from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)
num3 = randint(1, 10)
num4 = randint(1, 10)
num5 = randint(1, 10)

numerosRandomicos = (num1, num2, num3, num4, num5)

print(sorted(numerosRandomicos))

print(f"Menor Número: {sorted(numerosRandomicos)[0]}\nMaior Número: {sorted(numerosRandomicos)[4]}")
