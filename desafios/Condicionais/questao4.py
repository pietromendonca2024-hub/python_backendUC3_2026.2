"""
4.	Sistema de acesso
•	Peça usuário e senha.
•	Se usuário for "admin" e senha "1234", mostre "Bem-vindo!".
•	Caso contrário, "Usuário ou senha incorretos.".

"""
user = input("Digite o nome de usuário: ")
password = input("Digite a senha: ")
if user == "admin" and password == "1234":
    print("Bem-vindo!")
else:
    print("Usuário ou senha incorretos.")