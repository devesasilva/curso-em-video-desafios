'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre 
o comprimento da hipotenusa.
'''
#Resolução com módulo
import math
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimento do cateto adjacente: '))

hip = math.hypot(co, ca)
print(f'Segundo o comprimento dos catetos, {co} e {ca}, a hipotenusa equivale a {hip:.2f}')


#Resolução sem módulo
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimento do cateto oposto: '))

hip = (co ** 2 + ca ** 2) ** (1/2)
print(f'Segundo o comprimento do cateto oposto {co} e do cateto adjacente {ca}, a hipotenusa do triângulo retângulo corresponde a {hip}')