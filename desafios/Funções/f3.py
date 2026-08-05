"""
3. Função que calcula o fatorial usando FOR
Crie uma função fatorial(n) que usa um for para calcular o fatorial de um número.
"""
def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

print(fatorial(5))  