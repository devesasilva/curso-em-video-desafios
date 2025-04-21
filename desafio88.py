'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 
'''
# Exercício bem dificil para mim, vou tentar revisar posteriormene.

from random import randint

quantidade_jogos = int(input("Quantos jogos pretende fazer? "))
total_jogos = []

for i in range(quantidade_jogos):
    jogo = []

    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    total_jogos.append(jogo)

print("Os palpites gerados foram: ")
for i, jogo in enumerate(total_jogos, 1):
    print(f"Jogo {i}: {jogo}")

# A solução do Guanabara me deixou mais confusa