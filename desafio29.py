'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.
'''
vel = float(input('Insira a velocidade do carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'Você foi multado. Você deve pagar R$ {multa:.2f}')
else:
    print('Você não foi multado')