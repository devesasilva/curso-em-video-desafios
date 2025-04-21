#05 - Faça um programa que leia um número inteiro e mostre o seu sucessor e seu antecessor

n = int(input('Insira um número: '))
s = n + 1
a = n - 1
print(f'O sucessor do número inserido é {s} e o seu antecessor é {a}')

#Outra forma de resolver
n = int(input('Digite um número: '))
print(f'Analisando o número digitado {n}, o seu sucessor é {n+1} e o seu antecessor é {n-1}')