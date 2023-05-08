# Faça um programa que leia a largura e a altura de uma 
# parede em metros, calcule a sua área e a quantidade de tinta 
# necessária para pintá-la, sabendo que cada litro de tinta pinta 
# uma área de 2 metros quadrados.
largura = float(input("Digite o valor da largura: "))
altura = float(input("Digite o valor da altura: "))
area = largura * altura
tinta = area / 2
print(f"Sua parede tem as dimensões de {largura}x{altura} e sua a area é de {area}m2.\nPara pintar essa parede, você precisará de {tinta}L de tinta")