"""
8. Função que conta números pares em um intervalo
Exemplo: contar_pares(1, 20) → quantos pares existem?
"""
def contar_pares(inicio, fim):
    if inicio > fim:
        return "O valor inicial deve ser menor ou igual ao valor final."
    else:
        count = 0
        for num in range(inicio, fim + 1):
            if num % 2 == 0:
                count += 1
        return f"Existem {count} números pares entre {inicio} e {fim}."

print(contar_pares(1, 20))