'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8  
'''
n = int(input('Quantos termos você quer? '))
t1 = 0
t2 = 1
c = 3 # é 3 pq é um valor minimo para se ter uma sequência maior, uma que o resultado não seja só 0 e 1, que aparece no programa de qualquer forma.
print(f'{t1} -> {t2}', end= ' ')
while c <= n:
    t3 = t1 + t2
    c += 1
    t1 = t2
    t2 = t3
    print(f' -> {t3}', end=' ')
print('FIM')

n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=' -> ')
c = 3 # é 3 pq é um valor minimo para se ter uma sequência maior, uma que o resultado não seja só 0 e 1, que aparece no programa de qualquer forma.
while c <= n:
    t3 = t1 + t2
    c += 1
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
print('FIM')
