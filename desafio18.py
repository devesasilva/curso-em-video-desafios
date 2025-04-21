#18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Insira o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'Segundo o ângulo informado {ang}, seu seno é {sen:.2f}, seu cosseno é {cos:.2f} e sua tangente é {tan:.2f}:') 
