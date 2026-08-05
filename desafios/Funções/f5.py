"""
5. Função que soma valores até o usuário digitar 0
Use while + break.
"""
def somar_valores():
    soma = 0
    while True:
        try:
            valor = float(input("Digite um número (ou 0 para sair): "))
            if valor == 0:
                break
            soma += valor
        except ValueError:
            print("Por favor, insira um número válido.")
    return soma
    print(somar_valores())