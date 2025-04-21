'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
'''
nome = str(input('Digite o seu nome: ')).strip()
print(f'Você possui SILVA no nome? {'silva' in nome.lower()}')