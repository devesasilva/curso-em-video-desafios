'''
Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA (Progressão Aritmética), mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
c = 1
while c <= 10:
    print(termo, end= ' -> ')
    termo += razão
    c += 1
print('FIM')