"""
1. Função que verifica se o número é par ou ímpar
Crie uma função verificar par(num) que receba um número e diga se é par ou ímpar usando if.

"""
def verificar_par(num):
    if num % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

print(verificar_par(4))  