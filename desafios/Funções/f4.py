"""
4. Função que imprime números de 1 até N usando WHILE
Crie uma função contar(n) que utiliza um while para imprimir números até n.
"""
def contar(n):
    if n < 1:
        return "Por favor, insira um número maior ou igual a 1."
    else:
        i = 1
        numeros = []
        while i <= n:
            numeros.append(i)
            i += 1
        return numeros

print(contar(10))  