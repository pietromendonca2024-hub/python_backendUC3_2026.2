"""
1 - Leitura repetida até entrada válida
Objetivo: usar while para validar input.
Passos:
•	Pergunte por um número positivo.
•	Repita enquanto entrada inválida.
"""
while True:
    try:
        numero = float(input("Digite um número positivo: "))
        if numero > 0:
            print(f"Você digitou o número positivo: {numero}")
            break
        else:
            print("Número inválido. Por favor, digite um número positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")