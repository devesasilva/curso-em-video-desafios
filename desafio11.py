'''
11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária parar pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
'''
l = float(input('Insira a largura da parede em metros: '))
a = float(input('Insira a altura da parede em metros: '))
area = l * a  
print(f'A dimensão da sua parede é de {l}x{a} e sua área é de {area} m². Para pintar essa parede, será necessário {area / 2}')