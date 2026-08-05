"""
10. Função que retorna uma tabuada
Exemplo: tabuada(7)
 Use for para imprimir de 1 a 10.
"""
def tabuada(n):
    if n < 1:
        return "Por favor, insira um número maior ou igual a 1."
    else:
        resultado = []
        for i in range(1, 11):
            resultado.append(f"{n} x {i} = {n * i}")
        return resultado
print(tabuada(7))