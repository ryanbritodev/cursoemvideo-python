largura = float(input("Digite a largura da sua parede em metros: "))
altura = float(input("Digite a altura da sua parede em metros: "))

area = altura * largura
tinta = area / 2

print("Sua parede tem a dimensão de {:.1f}x{:.1f} e sua área é de {:.1f}m²\nSerão necessários {:.1f}L de tinta para realizar a pintura!".format(largura, altura, area, tinta))
