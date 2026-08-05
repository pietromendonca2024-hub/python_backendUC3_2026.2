"""
2. Função que retorna o maior de dois números
Crie uma função maior(a, b) que devolve qual número é maior usando if/else.
"""
def maior(a, b):
    if a > b:
        return f"O maior número é {a}."
    elif b > a:
        return f"O maior número é {b}."
    else:
        return "Os números são iguais."

print(maior(10, 5))  