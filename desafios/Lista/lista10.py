"""Questão 10
Solicite ao usuário que digite 5 números.
Armazene esses números em uma lista.
Ao final, exiba:
•	A lista completa. 
•	A soma dos números digitados.
"""
numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    
print("Lista completa:", numeros)
print("Soma dos números:", sum(numeros))