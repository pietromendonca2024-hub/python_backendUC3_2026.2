"""
7 - continue para pular negativos
•	Objetivo: somar números positivos da lista [-1,2,-3,4], pulando negativos com continue.
•	Usar: for, continue.
•	Dica: if n < 0: continue.
"""
numeros = [-1, 2, -3, 4]
soma = 0
for n in numeros:
    if n < 0:
        continue
    soma += n
print(f"Soma dos números positivos: {soma}")

