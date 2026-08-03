"""
6 - break para senha
•	Objetivo: pedir senha até acertar (senha = "senha123") — use while e break.
•	Usar: while, break.
•	Dica: quando acertar, faça break.
"""
senha_correta = "senha123"
while True:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso permitido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")