'''
Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
n = int(input('Escolha um número inteiro para ver a sua tabuada: '))
for m in range(1, 11):
    print(f'{n} X {m:2} = {n * m}')
