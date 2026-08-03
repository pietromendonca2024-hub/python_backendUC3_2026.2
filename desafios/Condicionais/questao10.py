"""
10.	Crie um menu de escolha utilizando número a escolha tem de ser 1 a 5 e no final deve mostrar o número escolhido.
"""
print("Menu de Escolha:")
print("1. Opção 1")
print("2. Opção 2")
print("3. Opção 3")
print("4. Opção 4")
print("5. Opção 5")

choice = int(input("Escolha uma opção (1-5): "))
if 1 <= choice <= 5:
    print(f"Você escolheu a opção {choice}.")
else:
    print("Opção inválida. Por favor, escolha um número de 1 a 5.")