"""
6. Função que cria um menu simples
Use while para repetir e if para opções:
1 – Somar
 2 – Subtrair
 0 – Sair
"""
def menu():
    while True:
        print("Menu:")
        print("1 – Somar")
        print("2 – Subtrair")
        print("0 – Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 + num2
                print(f"O resultado da soma é: {resultado}")
            except ValueError:
                print("Por favor, insira números válidos.")
        elif opcao == "2":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
            except ValueError:
                print("Por favor, insira números válidos.")
        elif opcao == "0":
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")
print(menu())