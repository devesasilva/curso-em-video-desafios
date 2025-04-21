'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = maior = somacoluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para {[l],[c]}: "))
       
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz[l][c] % 2 == 0: # Verifica quais o números pares 
            somapares += matriz[l][c] # Armazena e soma os números pares
    print()

for l in range(0, 3): # Soma dos valores da terceira coluna
    somacoluna+= matriz[l][2]

for c in range(0, 3): # Verifica qual o maior número na segunda linha
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f"A soma dos valores pares é {somapares}")
print(f"A soma dos valores da terceira coluna é {somacoluna}")
print(f"O maior valor da segunda linha é {maior}")
