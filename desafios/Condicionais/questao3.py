"""
2.	Verificação de idade mínima
•	Peça a idade do usuário.
•	Se for maior ou igual a 18, exiba "Acesso liberado ao sistema.".
Se for menor que 18, exiba "Acesso negado ao sistema.".
"""
age = int(input("Digite sua idade: "))
if age >= 18:
    print("Acesso liberado ao sistema.") 
else:
    print("Acesso negado ao sistema.")
