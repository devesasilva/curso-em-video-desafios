'''
Melhore o Desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(termo, end= ' -> ')
        termo += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quer exibir mais termos?\n[SIM] - Informe a quantidade \n[NÃO] - Digite 0.\n'))
print(f'No total foram {total} termos exibidos.')