"""
4- Soma até zero
•	Objetivo: ler números até o usuário digitar 0; mostrar a soma.
•	Usar: while, input.
•	Dica: verifique antes de somar se o número é 0 para encerrar.
"""
soma = 0
while True:
    try:
        numero = float(input("Digite um número (0 para encerrar): "))
        if numero == 0:
            break
        soma += numero
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

print(f"A soma dos números digitados é: {soma}")