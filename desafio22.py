'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
'''
nome = str(input('Insira o seu nome completo: ')).strip()


print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
print(f'Seu nome possui {len(nome)-nome.count(' ')} letras')
#print(f'Seu primeiro nome possui {nome.find(' ')} letras')
separa = nome.split()
print(f'Seu primeiro nome possui {len(separa[0])} letras')