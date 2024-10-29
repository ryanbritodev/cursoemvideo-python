# Modularização
# Modularização é o ato de construir módulos
# Surgiu no início da década de 60
# Sistemas ficando cada vez maiores
# Ajuda na divisão de um programa grande, aumentando a legibilidade
# Facilita na Organização do seu Código
# Facilita na manutenção
# Ocultação de código detalhado
# Reutilização em outros projetos

from uteis import numeros

# ou
# import uteis

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}")
print(f"O triplo de {num} é {numeros.triplo(num)}")
