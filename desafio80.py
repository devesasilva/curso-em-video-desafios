'''
Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela. 
'''
valores = []
for v in range(0, 5):
    n = int(input('Digite um valor: '))
    if v == 0 or n > valores[-1]:
        valores.append(n)
        print(f'Valor adicionado ao fim da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print(valores)