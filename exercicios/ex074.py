from random import randint

print(""" _   _   __                                             
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___               
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|              
| |\  | |_| | | | | | |  __/ | | (_) \__ \              
|_|_\_|\__,_|_| |_| |_|\_//\_|  \___/|___/              
|  _ \ __ _ _ __   __| ||/_\| _ __ ___ (_) ___ ___  ___ 
| |_) / _` | '_ \ / _` |/ _ \| '_ ` _ \| |/ __/ _ \/ __|
|  _ < (_| | | | | (_| | (_) | | | | | | | (_| (_) \__ |
|_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|_|\___\___/|___/\n""")

numerosRandomicos = (randint(1, 10), randint(1, 10),
                     randint(1, 10), randint(1, 10),
                     randint(1, 10))

print(f"Os números sorteados foram: ", end="")

for n in numerosRandomicos:
    print(f"{n} ", end="")

print(f"\nMaior Número: {max(numerosRandomicos)}\nMenor Número: {min(numerosRandomicos)}")
