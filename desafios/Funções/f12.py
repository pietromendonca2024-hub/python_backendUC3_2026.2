"""
12. Função que imprime apenas números ímpares pulando múltiplos de 7
Use for + continue.

"""
def imprimir_impares(n):
    if n < 1:
        return "Por favor, insira um número maior ou igual a 1."
    else:
        numeros = []
        for i in range(1, n + 1):
            if i % 2 == 0 or i % 7 == 0:
                continue
            numeros.append(i)
        return numeros

print(imprimir_impares(20))