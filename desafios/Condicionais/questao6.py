"""
6.	Verificação de estoque
•	Peça quantidade disponível e quantidade pedida.
•	Se o pedido for maior que o estoque, exiba "Estoque insuficiente.".
•	Caso contrário, "Pedido confirmado.".
"""
available_quantity = int(input("Digite a quantidade disponível: "))
requested_quantity = int(input("Digite a quantidade pedida: "))
if requested_quantity > available_quantity:
    print("Estoque insuficiente.")
else:
    print("Pedido confirmado.")